import streamlit as st 

st.title("Course Manager")
st.subheader ("Course Assignments Manager")
st.header("Course Assignments Manager")

st.divider()

assignments = [
    {
        "id": "HW1",
        "title" : "Intro to database",
        "description": "basics of database design",
        "points" : 100, 
        "type": "homework"
    } ,
    { 
        "id": "HW2",
        "title": "Normalization",
        "description": "normalizing",
        "points" : 100,
        "type": "homework"

    }
]#3 add new assignment 

st.subheader("Add New Assignemnt")

with st.container (border= True): 

    col1,col2=st.columns([2,1])


    with col1: 
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input ("Assignment title", placeholder= "homework1", help ="enter a name")
            description= st.text_area ("Assignment Description", placeholder= "ex.details...")

    with col2:
        st.markdown("**Due Date Selection**")
        due_date =st.date_input("Due Date")