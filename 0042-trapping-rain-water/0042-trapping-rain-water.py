class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_most, right_most = height[left], height[right]
        volume = 0

        while left < right:
            left_most = max(left_most, height[left])
            right_most = max(right_most, height[right])

            if left_most <= right_most:
                volume += left_most - height[left]
                left += 1
            else:
                volume += right_most - height[right]
                right -= 1

        return volume
