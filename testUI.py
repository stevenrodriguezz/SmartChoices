import streamlit as st

# Define a function for each page
def home():
    st.title("Smart Choices")
    st.write("Thank you for playing our game!")
    st.write("Are you proctoring the game or playing?")

def page2():
    st.title("Proctor Sign-In")
    st.write("Verification Step: Please Log-in:")

def page3():
    st.title("Session Selection")
    st.write("Please Enter the Room ID to join a game")

def page4():
    st.title("New Game or Continuation?")
    st.write("Please select an option below")

def page5():
    st.title("Game Start")
    st.write("Please enter how many players are playing your game")

def page6():
    key = "5J9QS7"
    st.title(f"Lobby     Key: {key}")
    st.write("wait for students to join your game")

# Initialize session state for navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define functions to change the page
def go_to_page6():
    st.session_state.page = 'page6'

def go_to_page5():
    st.session_state.page = 'page5'

def go_to_page4():
    st.session_state.page = 'page4'

def go_to_page3():
    st.session_state.page = 'page3'

def go_to_page2():
    st.session_state.page = 'page2'

def go_to_home():
    st.session_state.page = 'home'

# Render the selected page
if st.session_state.page == 'home':
    home()
    st.button('Proctor', on_click=go_to_page2)
    st.button('Player', on_click=go_to_page3)
elif st.session_state.page == 'page2':
    page2()
    st.text_input("Enter password:", type="password")
    go_to_page4()
elif st.session_state.page == 'page3':
    page3()
    room_id = st.text_input("Room ID")
elif st.session_state.page == 'page4':
    page4()
    st.button('New Game', on_click=go_to_page5)
    st.button('Continuation', on_click=go_to_home)
elif st.session_state.page == 'page5':
    page5()
    number_of_players = int(st.text_input("Number of Players", value = 0))
    go_to_page6()
elif st.session_state.page == 'page6':
    page6()