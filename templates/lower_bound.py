import bisect
from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        mid = (r + l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l


print(lower_bound([1, 2, 3, 4], 2), "==", bisect.bisect_left([1, 2, 3, 4], 2))
print(lower_bound([1, 2, 2, 2, 3, 4], 2), "==",
      bisect.bisect_left([1, 2, 2, 2, 3, 4], 2))
print(lower_bound([1, 2, 2, 2, 2, 3, 4], 2), "==",
      bisect.bisect_left([1, 2, 2, 2, 2, 3, 4], 2))
print(lower_bound([1, 2, 2, 2, 2, 3, 4], 5), "==",
      bisect.bisect_left([1, 2, 2, 2, 2, 3, 4], 5))
print(lower_bound([1, 2, 2, 2, 2, 3, 4], 0), "==",
      bisect.bisect_left([1, 2, 2, 2, 2, 3, 4], 0))
