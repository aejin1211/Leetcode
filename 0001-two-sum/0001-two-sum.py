class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[n] = i
        