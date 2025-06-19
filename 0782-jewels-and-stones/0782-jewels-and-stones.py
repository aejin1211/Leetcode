class Solution:
    def numJewelsInStones(self, cc: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in cc:
            count += freqs[char]
            
        return count

