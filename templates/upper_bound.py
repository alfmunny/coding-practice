from typing import List
import bisect


# find out the first element in list which is greater than the target
def upper_bound(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l


print(upper_bound([1, 2, 3, 4], 2), "==", bisect.bisect_right([1, 2, 3, 4], 2))
print(upper_bound([1, 2, 2, 2, 3, 4], 2), "==",
      bisect.bisect_right([1, 2, 2, 2, 3, 4], 2))
print(upper_bound([1, 2, 2, 2, 2, 3, 4], 2), "==",
      bisect.bisect_right([1, 2, 2, 2, 2, 3, 4], 2))
print(upper_bound([1, 2, 2, 2, 2, 3, 4], 5), "==",
      bisect.bisect_right([1, 2, 2, 2, 2, 3, 4], 5))
print(upper_bound([1, 2, 2, 2, 2, 3, 4], 0), "==",
      bisect.bisect_right([1, 2, 2, 2, 2, 3, 4], 0))
