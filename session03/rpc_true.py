import random

player_move = input("rock, paper or scissors? ").lower()
computer_move = random.choice(["rock", "paper", "scissors"])

if player_move not in ["rock", "paper", "scissors"]:
    print("Invalid choice")
    exit()
else:
    print(f"Computer: {computer_move}")



if player_move == computer_move:
    print("Draw!")
elif (player_move == "rock" and computer_move == "scissors") or \
     (player_move == "paper" and computer_move == "rock") or \
     (player_move == "scissors" and computer_move == "paper"):
    print("You win!")
else:
    print("Computer wins!")