import streamlit as st
from streamlit_ui.home import main as home_main
from streamlit_ui.chatbot import main as chatbot_main

# Sidebar for navigation
st.set_page_config(layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", (":house: Home", ":robot_face: SQL Chatbot"))

# Display pages based on selection
if page == ":house: Home":
    home_main()
elif page == ":robot_face: SQL Chatbot":
    chatbot_main()
