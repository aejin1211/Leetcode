class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #sort the array
        # no duplicates
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = n + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
        return res

