from typing import List

class Solution:
    def numberOfComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = list(range(n))

        def find(u):
            if u != uf[u]:
                uf[u] = find(uf[u])
            return uf[u]

        def union(uv):
            pu, pv = map(find, uv)
            if pu == pv:
                return False
            uf[pu] = pv
            return True

        return n - sum(map(union, edges))

