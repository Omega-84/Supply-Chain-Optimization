import streamlit as st
import numpy as np
from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable, lpSum, LpStatusOptimal

def run_modeling():
    # Create the optimization models
    min_model = LpProblem("Distribution Planning", LpMinimize)
    max_model = LpProblem("Distribution Planning", LpMaximize)
    
    # Create decision variables for each (warehouse, product, customer) combination
    X_min = LpVariable.dicts(
        "ship",
        [(w, p, c) for c in st.session_state["customers"]
         for p in st.session_state["products"]
         for w in st.session_state["warehouses"]],
        lowBound=0,
        cat="Integer"
    )
    X_max = LpVariable.dicts(
        "ship",
        [(w, p, c) for c in st.session_state["customers"]
         for p in st.session_state["products"]
         for w in st.session_state["warehouses"]],
        lowBound=0,
        cat="Integer"
    )
    
    # Objective functions: minimize and maximize shipping costs
    min_model += lpSum(
        X_min[(w, p, c)] * st.session_state["costs"].loc[(w, p), c]
        for c in st.session_state["customers"]
        for p in st.session_state["products"]
        for w in st.session_state["warehouses"]
    )
    max_model += lpSum(
        X_max[(w, p, c)] * st.session_state["costs"].loc[(w, p), c]
        for c in st.session_state["customers"]
        for p in st.session_state["products"]
        for w in st.session_state["warehouses"]
    )
    
    # Constraints: shipments from all warehouses must meet demand for each product and customer
    for c in st.session_state["customers"]:
        for p in st.session_state["products"]:
            min_model += lpSum([X_min[(w, p, c)] for w in st.session_state["warehouses"]]) == st.session_state["demand"].loc[p, c]
            max_model += lpSum([X_max[(w, p, c)] for w in st.session_state["warehouses"]]) == st.session_state["demand"].loc[p, c]
    
    # Solve the models
    min_status = min_model.solve()
    max_status = max_model.solve()
    
    if min_model.status == LpStatusOptimal and max_model.status == LpStatusOptimal:
        # Build and display the solution for the minimization model
        solns_min = st.session_state["costs"].copy()
        solns_min.values[:, :] = 0
        for w in st.session_state["warehouses"]:
            for p in st.session_state["products"]:
                for c in st.session_state["customers"]:
                    solns_min.loc[(w, p), c] = X_min[(w, p, c)].varValue
        
        # Similarly, build the worst-case solution (if needed)
        solns_max = st.session_state["costs"].copy()
        solns_max.values[:, :] = 0
        for w in st.session_state["warehouses"]:
            for p in st.session_state["products"]:
                for c in st.session_state["customers"]:
                    solns_max.loc[(w, p), c] = X_max[(w, p, c)].varValue
        
        final_cost = np.dot(st.session_state["costs"].to_numpy().flatten(),
                              solns_min.to_numpy().flatten())
        max_cost = np.dot(st.session_state["costs"].to_numpy().flatten(),
                          solns_max.to_numpy().flatten())
        savings = round((max_cost - final_cost) / max_cost * 100)
        
        st.header("The optimum quantities to ship from each warehouse are")
        st.table(solns_min)
        st.subheader(f"Total Shipping Cost: ${final_cost}")
        st.subheader(f"Savings: {savings}% compared to the maximum cost scenario")
    else:
        st.error("No optimal solution exists. Please verify your inputs and try again.")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Again"):
            st.session_state.clear()
            st.rerun()
    with col2:
        if st.button("🚪 Exit"):
            st.success("Thank you for using the app! Closing the session...")
            st.stop()
            import os
            os._exit(0)
