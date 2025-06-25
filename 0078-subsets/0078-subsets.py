class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(path, start):
            results.append(path)
            for i in range(start, len(nums)):
                
                dfs(path + [nums[i]], i+1)

        dfs([],0)
        return results