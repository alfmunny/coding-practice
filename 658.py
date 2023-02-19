from typing import List

class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - k

    while l < r:
      mid = (l + r) // 2
      if arr[mid+k] - x >= x - arr[mid]:
        r = mid
      else:
        l = mid + 1

    return arr[l:l+k]




