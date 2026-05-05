class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #val: index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [i, dict[diff]]
            dict[n] = i
        

