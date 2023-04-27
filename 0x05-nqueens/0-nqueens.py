#!/usr/bin/python3
import sys

def nqueens(N):
    # Create an empty board
    board = [[0 for x in range(N)] for y in range(N)]

    # Helper function to check if a queen can be placed at a given position
    def can_place(row, col):
        # Check row
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        # Check lower diagonal
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    # Recursive function to place queens on the board
    def place_queen(col):
        # Base case: all queens have been placed
        if col == N:
            # Print the solution
            for row in range(N):
                for col in range(N):
                    print(board[row][col], end=' ')
                print()
            print()
            return True

        # Try placing a queen in each row of the current column
        for row in range(N):
            if can_place(row, col):
                board[row][col] = 1
                place_queen(col+1)
                board[row][col] = 0

    # Start the recursive function
    place_queen(0)

# Check if the program was called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Parse the argument and check if it is a valid integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the N queens problem and print the solutions
nqueens(N)
