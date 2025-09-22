class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10**9 + 7
        ranges.sort(key=lambda x: x[0])
        count = 0
        last_end = -1

        for start, end in ranges:
            if start > last_end:
                count += 1
                last_end = end
            else:
                last_end = max(last_end, end)

        return pow(2, count, mod)
        

        