"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
            ]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # To make counting elements easy
    flat_board = sum(board, [])
    # Counting individual count of X and Y
    x_count = flat_board.count("X")
    o_count = flat_board.count("O")

    # First turn is always of "X" and if both counts are equal it implies next turn is of X
    if x_count == o_count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    # Loop over each individual item in the 2d list of board's elements to track emtpy slots
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible_moves.add((r,c))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid Move")

    temp_board = copy.deepcopy(board)

    temp_board[i][j] = player(board)

    return temp_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] is not EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] is not EMPTY:
                return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] is not EMPTY:
        return board[1][1]
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    state = winner(board)
    if state != None:
        return True

    for row in board:
        for col in board:
            if col is not EMPTY:
                return True
    return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    state = winner(board)
    if state == 'X':
        return 1
    elif state == 'O':
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board), None
    
    







# Helper functions

def is_maximizing(board):
    return player(board) == "X"
