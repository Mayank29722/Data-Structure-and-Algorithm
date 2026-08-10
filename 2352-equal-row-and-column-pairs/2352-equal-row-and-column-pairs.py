class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import Counter

        n = len(grid)

        # Count all rows
        rows = Counter(tuple(row) for row in grid)

        ans = 0

        # Check every column
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            ans += rows[col]

        return ans