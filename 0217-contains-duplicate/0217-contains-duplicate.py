class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if hash and num in hash:
                return True 
            hash[num] = 1
        return False