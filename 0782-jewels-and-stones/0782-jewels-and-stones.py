class Solution:
    def numJewelsInStones(self, cc: str, stones: str) -> int:
        return sum(s in cc for s in stones)