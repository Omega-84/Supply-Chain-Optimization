import streamlit as st
import numpy as np
import pandas as pd

def run_inputs():
    st.header("Input Data")
    st.markdown("Provide demand and cost data.")
    col1, col2 = st.columns(2)
    
    # Initialize flags if not set already
    st.session_state.setdefault("random_generated", False)
    st.session_state.setdefault("manual_input", False)
    
    # Option 1: Randomized Data
    with col1:
        if st.button("🎲 Randomize Values"):
            def random_demand_generator():
                return [np.random.randint(10, 40) for _ in range(st.session_state["num_products"])]
            def random_cost_generator():
                return [np.random.randint(70, 200) for _ in range(st.session_state["num_customers"])]
            
            st.session_state["demand"] = pd.DataFrame(
                {c: random_demand_generator() for c in st.session_state["customers"]},
                index=st.session_state["products"]
            )
            st.session_state["costs"] = pd.DataFrame(
                {(w, p): random_cost_generator() for w in st.session_state["warehouses"] for p in st.session_state["products"]},
                index=st.session_state["customers"]
            ).T
            st.session_state["random_generated"] = True
            st.session_state["manual_input"] = False  # reset manual flag if needed
    
    # If random data exists, display it and provide a way to continue
    if st.session_state.get("random_generated"):
        st.subheader("The demand across products is")
        st.table(st.session_state["demand"])
        st.subheader("The costs for production are")
        st.table(st.session_state["costs"])
        if st.button("✅ Save and Continue", key="save_random"):
            st.session_state["stage"] = "modeling"
            st.rerun()
    
    # Option 2: Manual Input
    if "manual_input" not in st.session_state:
        st.session_state["manual_input"] = False
    with col2:
        if st.button("✏️ Enter Values Manually"):
            st.session_state["manual_input"] = True
            st.session_state["random_generated"] = False  # reset random flag
    
    if st.session_state.get("manual_input"):
        st.header("Enter values for demand for each product")
        demand = st.data_editor(
            pd.DataFrame(np.zeros((st.session_state["num_products"], st.session_state["num_customers"])),
                         index=st.session_state["products"],
                         columns=st.session_state["customers"]),
            key="demand_df"
        )
        
        st.header("Enter values for cost for each product for each warehouse")
        cost = st.data_editor(
            pd.DataFrame(np.zeros((st.session_state["num_products"] * st.session_state["num_warehouses"], st.session_state["num_customers"])),
                         index=[(w, p) for w in st.session_state["warehouses"] for p in st.session_state["products"]],
                         columns=st.session_state["customers"]),
            key="cost_df"
        )
        
        if st.button("✅ Save and Continue", key="save_manual"):
            try:
                # Convert the user input to numeric values
                demand_numeric = demand.apply(pd.to_numeric, errors="raise")
                cost_numeric = cost.apply(pd.to_numeric, errors="raise")
                # Check if the cost DataFrame has a MultiIndex; if not, rebuild it
                if not isinstance(cost_numeric.index, pd.MultiIndex):
                    expected_index = [(w, p) for w in st.session_state["warehouses"] for p in st.session_state["products"]]
                    if len(cost_numeric.index) == len(expected_index):
                        cost_numeric.index = pd.MultiIndex.from_tuples(expected_index)
                    else:
                        st.error("Unexpected index structure for cost data. Please refresh the app and try again.")
                        return
                st.session_state["demand"] = demand_numeric
                st.session_state["costs"] = cost_numeric
                st.session_state["stage"] = "modeling"
                st.rerun()
            except Exception as e:
                st.error(f"Error in manual input data: {e}")
