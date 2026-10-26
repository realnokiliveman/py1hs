import random

wins = 0
losses = 0
draws = 0

while True:
    choice = input("rock, paper, scissors or q to quit: ")
    if choice == "q":
        break
    if choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice")
        continue

    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer:", computer)

    if choice == computer:
        print("Draw!")
        draws = draws + 1
    elif (choice == "rock" and computer == "scissors") or (choice == "paper" and computer == "rock") or (choice == "scissors" and computer == "paper"):
        print("You win!")
        wins = wins + 1
    else:
        print("You lose!")
        losses = losses + 1

print("You won", wins, end="")
print(", the computer won", losses, end="")
print(", draws:", draws)