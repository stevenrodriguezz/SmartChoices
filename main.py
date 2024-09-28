from utils import Player, start_game
from players import create_playerbase

number_of_players = 5
players = create_playerbase(number_of_players)

start_game(players)

players[1].investment_transaction(10000)
players[1].investment_accrual()

print(players[1].get_investment_account())