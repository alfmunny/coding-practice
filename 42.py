class Solution:
    def trap(self, height) -> int:
        ret = 0
        left_height = self.leftMaxHeights(height)
        right_height = self.rightMaxHeights(height)

        for i in range(len(height)):
            bar = min(left_height[i], right_height[i])
            if bar > height[i]:
                ret += bar - height[i]

        return ret

    def leftMaxHeights(self, height):
        max_left = 0
        ret = []
        for h in height:
            ret.append(max_left)
            max_left = max(max_left, h)
        return ret

    def rightMaxHeights(self, height):
        max_right = 0
        ret = []
        for h in reversed(height):
            ret.insert(0, max_right)
            max_right = max(max_right, h)
        return ret


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
