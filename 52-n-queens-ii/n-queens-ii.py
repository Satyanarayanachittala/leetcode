class Solution:
    def totalNQueens(self, n):
        cols = set()
        diag1 = set()
        diag2 = set()

        count = 0

        def backtrack(row):
            nonlocal count

            # All queens have been placed
            if row == n:
                count += 1
                return

            # Try every column
            for col in range(n):

                # Check if the position is attacked
                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return count