class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, num in enumerate(nums):
            dict[num] = i

        for i, num in enumerate(nums):
            if target - num in dict and dict[target-num] != i:
                return [i, dict[target - num]]
