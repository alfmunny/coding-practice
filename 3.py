from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        memo = defaultdict(int)

        # start together
        l = r = 0
        ret = 0

        while r < len(s):
            # check the window
            while l < r and memo[s[r]] > 0:
                memo[s[l]] -= 1
                l += 1

            memo[s[r]] += 1
            ret = max(ret, r - l + 1)
            r += 1

        return ret


print(Solution().lengthOfLongestSubstring("abcabcbb"))


