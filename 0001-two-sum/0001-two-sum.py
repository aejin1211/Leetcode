class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i, num in enumerate(nums):
            if target - num in dict_nums:
                return [i, dict_nums[target-num]]
            dict_nums[num] = i