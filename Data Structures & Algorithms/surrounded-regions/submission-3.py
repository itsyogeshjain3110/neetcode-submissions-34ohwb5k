class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        visit = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and board[nr][nc] == "O":
                        q.append((nr,nc))
                        visit.add((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r==rows-1 or c==cols-1:
                    if board[r][c] == "O":
                        bfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visit:
                    board[r][c] = "X"
