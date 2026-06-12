import streamlit as st

def loading_spinner(text: str = "Working..."):
    with st.spinner(text):
        pass
