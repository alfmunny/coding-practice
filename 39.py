from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, path, target):
            if target < 0:
                return

            if target == 0 and path:
                ans.append(path[:])
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, path, target-candidates[j])
                path.pop()

        dfs(0, [], target)

        return ans

s = Solution()

print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
