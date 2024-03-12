choices = {"pedra": 1, "papel": 2, "tesoura": 3, "lagarto": 4, "spock": 5}

player_1 = int(input("Write the value chosen by player 1 (1-5): "))
player_2 = int(input("Write the value chosen by player 2 (1-5): "))

if player_1 not in choices.values() or player_2 not in choices.values():
    print("Invalid choices. Make sure to choose an integer from 1 to 5.")
else:
    if player_1 == player_2:
        print("It's a tie!")
    elif (player_1, player_2) in [(1, 3), (1, 4), (2, 1), (2, 5), (3, 2), (3, 4), (4, 2), (4, 5), (5, 1), (5, 3)]:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")