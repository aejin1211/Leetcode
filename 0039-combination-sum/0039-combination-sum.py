class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(csum, start, path):
            if csum < 0:
                return
            if csum == 0:
                results.append(path[:])

            for i in range(start, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])        

        dfs(target, 0, [])
        return results