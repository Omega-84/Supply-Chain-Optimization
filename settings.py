import streamlit as st

def run_settings():
    st.set_page_config(
    page_title="Supply Chain Optimization",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)
    st.title("Supply Chain Optimization App")
    st.markdown(
    """
    ## Welcome to the Supply Chain Optimization App
    This application optimizes shipping strategies across warehouses. It is meant as a pure learning project but can has industry wide applications. 
    Use this tool to determine the optimal quantities to ship from warehouses to customers based on given demand and shipping costs.
    """
)

    st.markdown("Enter your supply chain parameters below:")
    
    # Get input values from the user and store them in session_state
    st.session_state["num_warehouses"] = int(st.number_input("Enter the number of warehouses:", min_value=1, key="warehouses_num"))
    st.session_state["warehouses"] = [f"W{i}" for i in range(1, st.session_state["num_warehouses"] + 1)]
    
    st.session_state["num_products"] = int(st.number_input("Enter the number of products:", min_value=1, key="products_num"))
    st.session_state["products"] = [f"P{i}" for i in range(1, st.session_state["num_products"] + 1)]
    
    st.session_state["num_customers"] = int(st.number_input("Enter the number of customers:", min_value=1, key="customers_num"))
    st.session_state["customers"] = [f"C{i}" for i in range(1, st.session_state["num_customers"] + 1)]
    
    if st.button("Next Steps"):
        st.session_state["stage"] = "inputs"
        # Use experimental_rerun() to refresh the app for the next stage
        st.rerun()
