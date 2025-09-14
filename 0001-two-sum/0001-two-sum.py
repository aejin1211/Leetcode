class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, num in enumerate(nums):
            dict_nums[num] = i
        
        for i, num in enumerate(nums):
            if target - num in dict_nums and i != dict_nums[target-num]:
                return [i, dict_nums[target-num]]