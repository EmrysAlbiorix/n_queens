def nqueens(n):
    # For n<1, n=2 and n=3 which have no solutions
    if n < 1 or n in [2, 3]:
        return False

    # Checks if it is safe to place queen at given position
    def safe(board, row, col):
        # Check row to the left
        for i in range(col):
            if board[i] == row:
                return False

        # Check upper diagonal to the left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[j] == i:
                return False
            i -= 1
            j -= 1

        # Check lower diagonal to the left
        i, j = row + 1, col - 1
        while i < n and j >= 0:
            if board[j] == i:
                return False
            i += 1
            j -= 1

        return True

    # Recursively tries to place queens column by column
    def solve(board, col):
        # If all queens are placed, return True
        if col >= n:
            return True

        # Try placing queen in each row of the current column
        for row in range(n):
            if safe(board, row, col):
                board[col] = row

                # Recursive step
                if solve(board, col + 1):
                    return True

                # If board[row][col] doesn't work remove the queen
                board[col] = 0

        return False

    # Initialize board with zeros
    board = [0] * n

    # Start placing queens from first column
    if solve(board, 0):
        return board
    return False