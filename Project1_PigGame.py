# pig game

import random


def roll_dice():
    minvalue = 1
    maxvalue = 6
    roll = random.randint(minvalue, maxvalue)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for indexes in range(players):
        print("\nPlayer number", indexes + 1, "turn has just started!")
        print("Your total score is:", player_scores[indexes], "\n")
        current_score = 0

        while True:
            roll = input("Would like to roll again (Enter y for yes)? ")

            # if it's other than y loop will break
            if roll.lower() != "y":
                break

            value = roll_dice()
            if value == 1:
                print("Rolled 1!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled :", value)

            print("player's score is:", current_score)

        player_scores[indexes] += current_score
        print("Total score= ", player_scores[indexes])

max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player ", winner + 1,
      "is the winner with a score of:", max_score)