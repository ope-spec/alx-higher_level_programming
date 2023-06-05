#!/usr/bin/python3
"""
A program that solves the N queens problem
"""

import sys


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print every possible solution.
    Parameters:
    - N (int): The number of queens and the size of the chessboard.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    print_solutions(solutions)


def solve_nqueens_util(board, col, solutions):
    """
    A recursive utility function to solve the N-Queens problem.
    Parameters:
    - board (list): The current state of the chessboard.
    - col (int): The current column to consider.
    - solutions (list): The list to store the solutions.
    """
    N = len(board)

    if col >= N:
        solution = []
        for row in range(N):
            queen_col = board[row].index(1)
            solution.append([row, queen_col])
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[row][col] = 0


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position.
    Parameters:
    - board (list): The current state of the chessboard.
    - row (int): The row to check.
    - col (int): The column to check.
    Returns:
    - bool: True if it is safe to place a queen, False otherwise.
    """
    N = len(board)

    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def print_solutions(solutions):
    """
    Print the solutions to the N-Queens problem.
    Parameters:
    - solutions: list of solutions.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
