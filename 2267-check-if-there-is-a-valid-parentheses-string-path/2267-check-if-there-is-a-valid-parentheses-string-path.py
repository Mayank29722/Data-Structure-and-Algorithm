class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] != "(":
            return False

        if grid[m - 1][n - 1] != ")":
            return False

        from functools import lru_cache

        @lru_cache(None)
        def dfs(row, col, balance):

            if balance < 0:
                return False

            remaining = (m - 1 - row) + (n - 1 - col)

            if balance > remaining:
                return False

            if row == m - 1 and col == n - 1:
                return balance == 0

            # Move down
            if row + 1 < m:
                if grid[row + 1][col] == "(":
                    if dfs(row + 1, col, balance + 1):
                        return True
                else:
                    if dfs(row + 1, col, balance - 1):
                        return True

            # Move right
            if col + 1 < n:
                if grid[row][col + 1] == "(":
                    if dfs(row, col + 1, balance + 1):
                        return True
                else:
                    if dfs(row, col + 1, balance - 1):
                        return True

            return False

        return dfs(0, 0, 1)