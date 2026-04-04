class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {}
        # value : index 

        for i, n in enumerate(nums):
            diff = target - n
            if val_map and diff in val_map:
                return [i, val_map[diff]]
            val_map[n] = i
            