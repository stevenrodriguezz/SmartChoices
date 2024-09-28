from utils import Player, start_game

Player1 = Player("Mechanic", 60000, 550)
Player2 = Player("Nurse", 90000, 630)
Player3 = Player("Grocer", 15000, 470)

players = [Player1, Player2, Player3]

start_game(players)

Player1.investment_transaction(10000)
Player1.investment_accrual()

print(Player1.get_investment_account())