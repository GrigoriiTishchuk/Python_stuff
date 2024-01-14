from random import randrange

"""
    Print the given board in a formatted way.
    Parameters:
        board (list): A list representing the board.
    Returns:
        None
"""
def print_board(board):
    print("---------")
    for row in board:
        print("|", " ".join(row), "|")
    print("---------")

"""
    Check if a player has won the game on the given board.
    Args:
        board (list): A 2-dimensional list representing the game board.
        player (any): The player to check for a win.
    Returns:
        bool: True if the player has won, False otherwise.
"""

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

"""
    Check if the board is a draw.
    Parameters:
    - board: a 2D list representing the game board
    Returns:
    - True if all cells in the board are not empty (' '), False otherwise
"""

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)


"""
    Takes a game board as input and prompts the user to enter their move. 
    It validates the move and returns the row and column corresponding to the move.
    Parameters:
        board (list): A 2D list representing the game board.
    Returns:
        tuple: A tuple containing the row and column of the valid move.
"""

def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if 1 <= move <= 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

"""
    Generate a random move for the computer player on the given board.
    Parameters:
    - board (list): A 2D list representing the game board.
    Returns:
    - tuple: A tuple containing the row and column indices of the randomly generated move.
"""

def computer_move(board):
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] == ' ':
            return row, col

"""
    Executes the main logic of the Tic-Tac-Toe game.

    This function initializes the game board, welcomes the players, and alternates between the user and the computer making moves until there is a winner or a draw.

    Parameters:
    None

    Returns:
    None
"""
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        user_row, user_col = user_move(board)
        board[user_row][user_col] = 'O'
        print_board(board)
        
        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            break
        elif is_draw(board):
            print("It's a tie!")
            break
        
        print("Computer's turn:")
        comp_row, comp_col = computer_move(board)
        board[comp_row][comp_col] = 'X'
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()