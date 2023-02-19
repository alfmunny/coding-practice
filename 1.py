from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    memo = {}

    for i, n in enumerate(nums):
      if target - n not in memo:
        memo[n] = i
      else:
        return [memo[target -n ], i]

    return []

