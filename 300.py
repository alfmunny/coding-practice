from typing import List

# brute force 
def LIS(nums: List[int]) -> int:
  if not nums:
    return 0
  ret = 0
  for i, n in enumerate(nums):
    temp = 1
    last_val = n
    for m in nums[i+1:]:
      if m > last_val:
        temp += 1
        last_val = m

    ret = max(ret, temp)

  return ret

print(LIS([10,9,2,5,3,7,101,18]))


# lower bound

class Solution():
  def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
      return 0
    seq = []
    for n in nums:
      p = self.lower_bound(seq, n)
      if p == len(seq):
        seq.append(n)
      else:
        seq[p] = n

    return len(seq)

  def lower_bound(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
      mid = (l + r) // 2

      if nums[mid] >= target:
        r = mid
      else:
        l = mid + 1

    return l

s = Solution();

print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
