class Solution:
    def numJewelsInStones(self, cc: str, stones: str) -> int:
        freqs = {}
        count = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in cc:
            if char in freqs:
                count += freqs[char]
        return count
        