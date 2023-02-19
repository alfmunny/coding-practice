from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        ans = []
        candidates.sort()

        def dfs(i, path, target):
            if target < 0:
                return

            if path and target == 0:
                ans.append(path[:])

            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                path.append(candidates[j])
                dfs(j+1, path, target - candidates[j])
                path.pop()

        dfs(0, [], target)

        return ans

s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
