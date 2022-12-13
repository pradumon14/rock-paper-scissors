# Import the random module to generate random numbers
import random

# Create a list of possible options
options = ["rock", "paper", "scissors"]

# Welcome the player and explain the rules
print("Welcome to Rock, Paper, Scissors!")
print("The rules are simple: choose rock, paper, or scissors.")
print("If your choice beats the computer's choice, you win!")

# Generate the computer's choice
computer_choice = random.choice(options)

# Ask the player for their choice
player_choice = input("What do you choose? ")

# Check if the player's choice is valid
if player_choice not in options:
  print("Sorry, that's not a valid option.")

# If the player's choice is valid, compare it to the computer's choice
else:
  # Display the player's choice and the computer's choice
  print("You chose " + player_choice + " and the computer chose " + computer_choice + ".")

  # Determine the winner
  if player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
  elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
  elif player_choice == computer_choice:
    print("It's a tie!")
  else:
    print("The computer wins!")
