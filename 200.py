from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = list(range(m*n))

        def find(u):
            if u != uf[u]:
                uf[u] = find(uf[u])
            return uf[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            uf[pu] = pv
            return True

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                ans += 1

                for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        if union(n*i + j, n*x + y):
                            ans -= 1

        return ans



grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()

print(s.numIslands(grid1))
print(s.numIslands(grid2))

# Union find

