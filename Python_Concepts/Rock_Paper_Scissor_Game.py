import random

choices = ["rock", "paper", "scissors"]
matrix = [[None, None, None],
          [None, None, None],
          [None, None, None]]

user_choice = input("Enter your choice (rock, paper, or scissors): ")
computer_choice = random.choice(choices)

print(f"Computer chooses: {computer_choice}")
print(f"You choose: {user_choice}")

if user_choice.lower() in choices:
    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice.lower() == "rock" and computer_choice == "scissors") or
        (user_choice.lower() == "paper" and computer_choice == "rock") or
        (user_choice.lower() == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose either rock, paper, or scissors.")

row = int(input("Enter the row number (0-2): "))
col = int(input("Enter the column number (0-2): "))

if row >= 0 and row < 3 and col >= 0 and col < 3:
    matrix[row][col] = user_choice.lower()
    print("Matrix after updating user choice:")
    for row in matrix:
        print(row)
else:
    print("Invalid row or column number. The matrix was not updated.")
