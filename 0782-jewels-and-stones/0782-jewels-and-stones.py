class Solution:
    def numJewelsInStones(self, cc: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for char in cc:
            count += freqs[char]
        return count
