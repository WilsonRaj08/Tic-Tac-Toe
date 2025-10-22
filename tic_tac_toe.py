import os
import time

# Initialize the board with empty spaces
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1  # Player 1 starts
Win = 1
Draw = -1
Running = 0
Game = Running
Mark = 'X'

# Clear screen (cross-platform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the Tic Tac Toe board
def DrawBoard():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")

# Function to check if a position is available
def CheckPosition(x):
    return board[x] == ' '

# Function to check if someone has won or the game is drawn
def CheckWin():
    global Game
    # Winning combinations
    win_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]
    for (x, y, z) in win_combinations:
        if board[x] == board[y] == board[z] and board[x] != ' ':
            Game = Win
            return
    if all(space != ' ' for space in board[1:]):
        Game = Draw
    else:
        Game = Running

# Game intro
print("-------- Welcome to TIC TAC TOE Game --------")
print()
print("-------- Designed By Anubhav Chakraborty --------")
print()

a = input("Enter name of Player 1 -> ")
b = input("Enter name of Player 2 -> ")
print("\nPlease Wait...")
time.sleep(2)

# Game loop
while Game == Running:
    clear_screen()
    DrawBoard()

    if player % 2 != 0:
        print(f"\n{a}'s turn (X)")
        Mark = 'X'
    else:
        print(f"\n{b}'s turn (O)")
        Mark = 'O'

    try:
        choice = int(input("Enter the position [1-9] where you want to mark: "))
        if choice < 1 or choice > 9:
            print("Invalid position! Choose between 1 and 9.")
            time.sleep(1)
            continue
        if CheckPosition(choice):
            board[choice] = Mark
            player += 1
            CheckWin()
        else:
            print("That position is already taken! Try again.")
            time.sleep(1)
    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)

# Final results
clear_screen()
DrawBoard()
print()
if Game == Draw:
    print("It's a Draw! 🤝")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print(f"🏆 {a} Wins! Congratulations!")
    else:
        print(f"🏆 {b} Wins! Congratulations!")
