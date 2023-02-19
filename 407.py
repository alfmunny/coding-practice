import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, [heightMap[i][j], i, j])
                    heightMap[i][j] = -1


        level = 0
        ret = 0

        while heap:
            h, i, j = heapq.heappop(heap)
            level = max(level, h)

            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if x < 0 or x >=m or y < 0 or y >= n or heightMap[x][y] == -1:
                    continue

                heapq.heappush(heap, [heightMap[x][y], x, y])

                if heightMap[x][y] < level:
                    ret += level - heightMap[x][y]

                heightMap[x][y] = -1


        return ret




