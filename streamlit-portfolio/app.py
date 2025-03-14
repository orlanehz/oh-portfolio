import streamlit as st
from projects import project1, project2, project3

st.title("My Portfolio")
st.write("Welcome to my portfolio. Here are my projects:")

# Personal Information
st.header("About Me")
st.write("""
Hi, I'm a Senior Data Analyst with 3 years of experience at Pernod Ricard in Marketing Mix Modelling, Power BI, dbt, SQL, and more. 
I hold a Master's degree in Data Science, specializing in AI, ML, Data Engineering, BI, etc.
""")

# Project Selectionrrr
project_options = ["Project 1", "Project 2", "Project 3"]
project_choice = st.selectbox("Choose a project to view", project_options)

if project_choice == "Project 1":
    project1.display()
elif project_choice == "Project 2":
    project2.display()
elif project_choice == "Project 3":
    project3.display()

def display():
    st.header("Project 1")
    st.write("Details about Project 1")