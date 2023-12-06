# ia.py

import random

def ia(board, signe):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if available_moves:
        return random.choice(available_moves)
    else:
        return None
