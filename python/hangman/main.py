
import random


def winner(board):
    """This function accepts the Connect Four board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return 'X', and if the computer has
    won it will return 'O'."""
    for row in range(7):
        count = 0
        last = ''
        for col in range(7):
            row_win = board[row][col]
            if row_win == " ":
                count = 0
                continue
            if row_win == last:
                count += 1
            else:
                count = 1
            if count >= 4:
                return row_win
            last = row_win

    for col in range(7):
        count = 0
        last = ''
        for row in range(7):
            col_win = board[row][col]
            if col_win == " ":
                count = 0
                continue
            if col_win == last:
                count += 1
            else:
                count = 1
            if count >= 4:
                return col_win
            last = col_win


    # No winner: return the empty string
    return ""


def display_board(board):
    """This function accepts the Connect Four board as a parameter.
    It will print the Connect Four board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays
    the column numbers on top of the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""

    print("   0   1   2   3   4   5   6")
    for row in range(7):
        print("   " + board[row][0] + " | " + board[row][1] + " | " + board[row][2] + " | " + board[row][3] + " | " + board[row][4] + " | " + board[row][5] + " | " + board[row][6])
        if row != 6:
            print("  ---+---+---+---+---+---+---")
    print()


def make_user_move(board):
    """This function accepts the Connect Four board as a parameter.
    It will ask the user for a row and column.  If the row and
    column are each within the range of 0 and 6, and that square
    is not already occupied, then it will place an 'X' in that square."""

    valid_move = False
    while not valid_move:
        try:
            col = int(input("What col would you like to move to (0-6):"))
            if board[0][col] != ' ':
                print("Sorry, that column is full. Please try again!\n")
            else:
                for row in range(6, -1, -1):
                    if board[row][col] == ' ' and not valid_move:
                        board[row][col] = 'X'
                        valid_move = True
        except:
            ValueError

    return board


def make_computer_move(board):
    """This function accepts the Connect Four board as a parameter.
    It will randomly pick row and column values between 0 and 6.
    If that square is not already occupied it will place an 'O'
    in that square.  Otherwise, another random row and column
    will be generated."""
    computer_valid_move = False
    while not computer_valid_move:
        col = random.randint(0, 6)
        if board[0][col] != ' ':
            print("Sorry, that column is full. Please try again!\n")
        else:
            for row in range(6, -1, -1):
                if board[row][col] == ' ' and not computer_valid_move:
                    board[row][col] = 'O'
                    computer_valid_move = True
    return board


def main():
    """The Main Game Loop:"""

    free_cells = 42
    users_turn = True
    ttt_board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            ttt_board = make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            ttt_board = make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print("Y O U   W O N !")
    elif (winner(ttt_board) == 'O'):
        print("I   W O N !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")



if __name__=='__main__':
    
    main()

