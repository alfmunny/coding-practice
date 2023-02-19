class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1

            while l < r:
                current_val = nums[i] + nums[l] + nums[r]
                if  current_val == target:
                    return target
                elif current_val > target:
                    r -= 1
                else:
                    l += 1

                if abs(current_val - target) < abs(ret - target):
                    ret = current_val

        return ret

