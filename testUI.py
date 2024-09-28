import streamlit as st

# Define a function for each page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def page2():
    st.title("Page 2")
    st.write("You are now on Page 2!")

def page3():
    st.title("Page 3")
    st.write("You are now on Page 3!")

# Initialize session state for navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define functions to change the page
def go_to_page3():
    st.session_state.page = 'page3'

def go_to_page2():
    st.session_state.page = 'page2'

def go_to_home():
    st.session_state.page = 'home'

# Render the selected page
if st.session_state.page == 'home':
    home()
    st.button('Go to Page 2', on_click=go_to_page2)
    st.button('Go to Page 3', on_click=go_to_page3)
elif st.session_state.page == 'page2':
    page2()
    st.button('Go to Home', on_click=go_to_home)
elif st.session_state.page == 'page3':
    page3()
    st.button('Go to Home', on_click=go_to_home)