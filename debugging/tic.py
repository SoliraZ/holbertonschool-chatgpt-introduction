#!/usr/bin/python3
def print_board(board):
    """Prints the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner"""
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Checks if the board is full"""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Runs the Tic-Tac-Toe game"""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        
        # Input validation for row and column
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Check if the row and column are within valid range
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2. Try again.")
                continue
            
            # Check if the cell is already occupied
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            # Make the move
            board[row][col] = player
            
            # Switch player
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input! Please enter integers only. Try again.")
        
        # Check for draw condition (no winner and board is full)
        if is_full(board) and not check_winner(board):
            print_board(board)
            print("The game is a draw!")
            return

    # Print the final board and winner
    print_board(board)
    print(f"Player {player} wins!")

# Start the game
tic_tac_toe()
