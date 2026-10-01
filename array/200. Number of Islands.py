from collections import deque


class Solution:
    def numIslands(self,grid:list[list[str]])->int:
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row ,col = q.popleft()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    r, c = row+dr , col + dc
                    if (r in range(rows) and c in range(colmns) and grid[r][c]=='1' and (r,c) not in  visit):
                        q.append((r,c))
                        visit.add((r,c))
        
        
        count = 0
        rows , colmns = len(grid) , len(grid[0])
        visit = set()
        for r in range(rows):
            for c in range(colmns):
                if grid[r][c] == '1' and not (r,c)in visit:
                    bfs(r,c)
                    count += 1
        return count

a = Solution()
print(a.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

