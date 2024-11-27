import streamlit as st
from function import socialMediaPage, profilePage, educationPage, mobileProgrammingPage,webProgrammingPage

def sideBar():
    st.sidebar.title("Navigation")
    
    page = st.sidebar.selectbox("Choose Page", ["Overall", "Profile Page", "Education", "Social Media"])
    if page == "Profile Page":
        profilePage()
    elif page == "Education":
        educationPage() 
    elif page == "Social Media":
        socialMediaPage()
    else:
        profilePage()
        col1, col2 = st.columns([1,1])
        with col1:
            educationPage()
        with col2:
            socialMediaPage()

    