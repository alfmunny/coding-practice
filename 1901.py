from typing import List

class Solution:
  def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    l, r = 0, len(mat) - 1

    while l < r:
      mid = (l + r) // 2

      if max(mat[mid]) > max(mat[mid+1]):
        r = mid
      else:
        l = mid + 1

    return [l, mat[l].index(max(mat[l]))]
