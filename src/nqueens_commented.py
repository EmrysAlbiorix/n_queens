def nqueens(n):
    """
    Solves the n-queens puzzle for a given board size n.
    The n-queens puzzle is the problem of placing n chess queens on an n×n chessboard
    so that no two queens threaten each other. Thus, a solution requires that no two
    queens share the same row, column, or diagonal.

    Args:
        n (int): Size of the chess board and number of queens to place

    Returns:
        list or False: A list representing the row positions for each queen (indexed by column),
                      or False if no solution exists

    Example:
        nqueens(4) returns [1, 3, 0, 2] representing a valid solution where:
        - Queen in column 0 is in row 1
        - Queen in column 1 is in row 3
        - Queen in column 2 is in row 0
        - Queen in column 3 is in row 2
    """

    # The n-queens puzzle has no solutions for n < 1 (invalid board size)
    # and n = 2 or 3 (mathematically impossible to place queens safely)
    if n < 1 or n in [2, 3]:
        return False

    def is_safe(board, row, col):
        """
        Checks if it's safe to place a queen at the given position.

        Args:
            board (list): Current state of the board
            row (int): Row to check
            col (int): Column to check

        Returns:
            bool: True if it's safe to place a queen, False otherwise

        Note: We only need to check to the left of the current column because:
        1. Queens haven't been placed to the right yet
        2. We're using a 1D array where the index represents the column and
           the value represents the row where the queen is placed
        """
        # Check row to the left
        # For each column to the left, see if a queen exists in the same row
        for i in range(col):
            if board[i] == row:
                return False

        # Check upper diagonal to the left
        # Move diagonally up and left, checking for queens
        # Zip is a built-in function in python that allows pairing
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[j] == i:
                return False

        # Check lower diagonal to the left
        # Move diagonally down and left, checking for queens
        for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
            if board[j] == i:
                return False

        return True

    def solve(board, col):
        """
        Recursively tries to place queens column by column using backtracking.

        Args:
            board (list): Current state of the board
            col (int): Current column to process

        Returns:
            bool: True if a solution is found, False otherwise
        """
        # Base case: If we've successfully placed queens in all columns
        # we've found a valid solution
        if col >= n:
            return True

        # Try placing a queen in each row of the current column
        for row in range(n):
            # Check if we can place a queen at this position
            if is_safe(board, row, col):
                # Place the queen
                board[col] = row

                # Recursively try to place queens in the remaining columns
                if solve(board, col + 1):
                    return True

                # If placing queen at board[row][col] doesn't lead to a solution,
                # remove queen from board[row][col] (backtrack) and try next row
                board[col] = 0

        # If we've tried all rows in this column and none work,
        # return False to trigger backtracking
        return False

    # Initialize board: index represents column, value represents row
    # Initialize with zeros as no queens are placed yet
    board = [0] * n

    # Start placing queens from the first column (col = 0)
    # If a solution is found, return the board state
    if solve(board, 0):
        return board

    # If no solution is found, return False
    return False