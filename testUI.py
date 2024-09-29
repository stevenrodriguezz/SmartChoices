import streamlit as st
import time
from utils import Player, start_game
from players import create_playerbase

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

def page7():
    st.title("Proctor Screen")
    st.write("Enable features, start next rounds, and monitor student progress")

def page8():
    st.title("Student Screen")

def page9():
    st.title("Pay Bills")

# Initialize session state for navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define functions to change the page
def go_to_page9():
    st.session_state.page = 'page9'

def go_to_page8():
    st.session_state.page = 'page8'

def go_to_page7():
    st.session_state.page = 'page7'

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

number_of_players = 15

image_urls = [
        "Astronaut.png",
        "https://via.placeholder.com/300?text=Avatar+2",
        "https://via.placeholder.com/300?text=Avatar+3",
        "https://via.placeholder.com/300?text=Avatar+4",
        "https://via.placeholder.com/300?text=Avatar+5",
        "https://via.placeholder.com/300?text=Avatar+6",
        "https://via.placeholder.com/300?text=Avatar+7",
        "https://via.placeholder.com/300?text=Avatar+8",
        "https://via.placeholder.com/300?text=Avatar+9"
        "https://via.placeholder.com/300?text=Avatar+10",
        "https://via.placeholder.com/300?text=Avatar+11",
        "https://via.placeholder.com/300?text=Avatar+12",
        "https://via.placeholder.com/300?text=Avatar+13",
        "https://via.placeholder.com/300?text=Avatar+14",
        "https://via.placeholder.com/300?text=Avatar+15"
    ]

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
    go_to_page8()
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
    col1, col2, col3 = st.columns([1, 1, 1])

    # Display the current image based on the index
    with col1:
        for i in range(0, int(number_of_players/3)):
            st.markdown(f"✅ player {i+1}")
            time.sleep(0.2)
    with col2:
        for i in range(int(number_of_players/3), int(number_of_players/3) + int(number_of_players/3)):
            st.markdown(f"✅ player {i+1}")
            time.sleep(0.2)
    with col3:
        for i in range(int(number_of_players/3) + int(number_of_players/3), number_of_players):
            st.markdown(f"✅ player {i+1}")
            time.sleep(0.2)
    st.button('Start Game', on_click=go_to_page7)
elif st.session_state.page == 'page7':
    page7()
    st.checkbox("Credit Cards")
    st.checkbox("Investments")
    st.checkbox("Emergencies")
    st.button('Start Next Round')

    players = create_playerbase(number_of_players)
    #start_game(players)

    # Initialize session state for index if not already set
    if 'img_index' not in st.session_state:
        st.session_state.img_index = 0

    # Function to update image index
    def next_image():
        if st.session_state.img_index < len(image_urls) - 1:
            st.session_state.img_index += 1

    def prev_image():
        if st.session_state.img_index > 0:
            st.session_state.img_index -= 1

    col1, col2, col3 = st.columns([1, 1, 1])

    # Display the current image based on the index
    with col2:
        st.image(image_urls[st.session_state.img_index])

    # Create navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])  # Layout for buttons

    with col1:
        if st.button("⬅️ Previous", key='prev'):
            prev_image()

    with col2:
        st.write(f"Player: {st.session_state.img_index + 1}")
        st.write(f"Budget for turn: {players[st.session_state.img_index].get_monthly_income()}")
        st.write(f"Budget used: {round(players[st.session_state.img_index].get_monthly_income() * 0.77, 2)}")
        if players[st.session_state.img_index].get_monthly_income() >= 5000:
            st.markdown("✅ completed turn")
        else:
            st.markdown("not done with turn yet")

    with col3:
        if st.button("Next ➡️", key='next'):
            next_image()
elif st.session_state.page == 'page8':
    page8()

    players = create_playerbase(number_of_players)
    start_game(players)

    # Initialize session state for index if not already set
    if 'img_index' not in st.session_state:
        st.session_state.img_index = 0

    # Function to update image index
    def next_image():
        if st.session_state.img_index < len(image_urls) - 1:
            st.session_state.img_index += 1

    def prev_image():
        if st.session_state.img_index > 0:
            st.session_state.img_index -= 1

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(image_urls[st.session_state.img_index])
        st.write("Your profession is:")
        st.write(f"{players[st.session_state.img_index].get_job()}")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("annual income")
    with col2:
        st.write("credit score")
    with col3:
        st.write("student loans")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write(f"{players[st.session_state.img_index].get_salary()}")
    with col2:
        st.write(f"{players[st.session_state.img_index].get_credit_score()}")
    with col3:
        st.write(f"{players[st.session_state.img_index].get_student_loans()}")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("monthly income")
    with col2:
        st.write("monthly taxes")
    with col3:
        st.write("debt")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write(f"{players[st.session_state.img_index].get_monthly_income()}")
    with col2:
        st.write(f"{players[st.session_state.img_index].get_monthly_taxes()}")
    with col3:
        st.write(f"{players[st.session_state.img_index].get_debt()}")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("budget remaining for month")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write(f"{players[st.session_state.img_index].get_bank()}")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button('Pay Bills', on_click=go_to_page9)
    with col2:
        st.button('Get Loan', on_click=go_to_page2, disabled=True)
    with col3:
        st.button('Invest', on_click=go_to_page2, disabled=True)

elif st.session_state.page == 'page9':
    page9()

    players = create_playerbase(number_of_players)
    start_game(players)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("budget for month")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write(f"{players[st.session_state.img_index].get_bank()}")

    col1, col2, col3 = st.columns([1, 1, 1])

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button('Return', on_click=go_to_page8)
    