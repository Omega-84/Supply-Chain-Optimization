import streamlit as st
from settings import run_settings
from input_data import run_inputs
from modeling import run_modeling

# Initialize the stage if not set (the first stage is "setting")
if "stage" not in st.session_state:
    st.session_state["stage"] = "setting"

# Direct the flow based on the current stage
if st.session_state["stage"] == "setting":
    run_settings()
elif st.session_state["stage"] == "inputs":
    run_inputs()
elif st.session_state["stage"] == "modeling":
    run_modeling()
