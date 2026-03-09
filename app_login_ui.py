import streamlit as st
import time 
import json
from pathlib import Path 
from datetime import datetime

st.set_page_config(page_title="Course Manager", page_icon="", layout="centered", initial_sidebar_state="collapsed")

json_file=("users.json")

#Load the data from a json file
if json_file.exists():
    with json_file.open("r", encoding="utf-8") as f:
        users=json.load(f)

users=[
    {
    "id": "1",
    "email": "admin@school.edu",
    "full_name": "System Admin",
    "password": "123ssag@43AE",
    "role": "Admin",
    "registered_at": "..."
}
]

json_path=Path("users.json")

#Load the data from a json file
if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        users=json.load(f)

tab1, tab2=st.tabs(["Log In", "Register"])

with tab1:
    with st.container(border=True):
        st.markdown("#Log In")
        user_name=st.text_input("Email")

        password=st.text_input("Password", type="password")

    
                   


    st.markdown("message")