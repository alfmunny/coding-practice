from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ret = 0

    while l < r:
      current_min = min(height[l], height[r])
      ret = max(ret, current_min * (r - l))

      while height[l] <= current_min and l < r:
        l += 1
      while height[r] <= current_min and l < r:
        r -=1

    return ret
