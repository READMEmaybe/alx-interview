#!/usr/bin/python3
"""N queens puzzle"""
import sys


def isSafe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for c in range(col):
        if board[c] == row or \
           board[c] + c == row + col or \
           board[c] - c == row - col:
            return False
    return True


def solveNQUtil(board, col):
    """Use backtracking to solve the N queens puzzle"""
    n = len(board)
    if col == n:
        print(str([[c, board[c]] for c in range(n)]))
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[col] = i
            solveNQUtil(board, col + 1)
            board[col] = -1


def nqueens(n):
    """Solve the N queens puzzle"""
    if n < 4:
        print("N must be at least 4")
        return
    board = [-1 for i in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
