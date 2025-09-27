class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i, num in enumerate(nums):
            if num in hash:
                return True
            hash[num] = i
        return False