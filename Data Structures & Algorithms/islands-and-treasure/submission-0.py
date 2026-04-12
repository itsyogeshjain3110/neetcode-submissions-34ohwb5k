class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        # append all treasures/gates in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        while q:
            row, col = q.popleft()
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in directions:
                nr, nc = row+dr, col+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] ==  2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append([nr,nc])

        