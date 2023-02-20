# N QUEENS PROBLEM - CLASSIC
# 
# A program in Python to solve the n-queens problem. That is, you have to place n queens on a nxn chessboard so that no queen can capture another queen.
# This solves the "N queens problem - classic" version of the problem.
# 
# In the modified problem, which we don't solve here, queens can also make knight moves. So, in that problem, one must also make sure that no queen
# can capture another using a knight move.

def solve_n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve_n_queens_helper(board, 0, solutions)
    return solutions

def solve_n_queens_helper(board, col, solutions):
    # Base case: all queens have been placed
    if col == len(board):
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_helper(board, col + 1, solutions)
            board[row][col] = 0

def is_safe(board, row, col):
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # All checks passed, it is safe to place a queen here
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if val == 1 else "." for val in row))
    print()

# Test the program with a 4x4 board
solutions = solve_n_queens(4)
for solution in solutions:
    print_board(solution)
