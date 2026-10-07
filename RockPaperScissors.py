#Create a game of rock, paper, scissors between the user and the computer

import random
#choices the player and computer can pick
valid_choices = ["rock", "paper", "scissors"]

# create custom functions
def get_player_choice():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while (player_choice not in valid_choices):
        player_choice = (input("Invalid input. Try again: ")).lower()
    return player_choice

def determine_winner(player_choice, computer_choice):
    if (player_choice == computer_choice):
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors"):
        return "win"
    elif (player_choice == "scissors" and computer_choice == "paper"):
        return "win"
    elif (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "loss"

# start game and ask for round count
print("Welcome to Rock, Paper, Scissors!")
round_count = int(input("How many rounds would you like to play? ")) 
player_wins = 0
computer_wins = 0
while round_count % 2 == 0:
    round_count = int(input("Invalid round count. Enter an odd number: "))

# run game and get wins and losses
while player_wins + computer_wins < round_count:
    player_choice = get_player_choice()
    computer_choice = random.choice(valid_choices)
    print("The computer chose " + computer_choice + ".")
    round_result = determine_winner(player_choice, computer_choice)
    if round_result == "win":
        print("You won!")
        player_wins += 1
    elif round_result == "loss":
        print("You lost!")
        computer_wins += 1
    elif round_result == "tie":
        print("Tie! Play again.")

# print game results
print("-------------")
print("Score - You: " + str(player_wins) + " || Computer: " + str(computer_wins))
if player_wins > computer_wins:
    print("YOU WIN!!!")
else:
    print("The computer wins!")
print("Thanks for playing!")
