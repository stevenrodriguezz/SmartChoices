from utils import Player, start_game

Player1 = Player("Mechanic", 60000)
Player2 = Player("Nurse", 90000)
Player3 = Player("Grocer", 15000)

players = [Player1, Player2, Player3]

start_game(players)
