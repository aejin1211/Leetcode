class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = collections.defaultdict(int)
        countT = collections.defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1

        for chac in countS:
            if countS[chac] != countT[chac]:
                return False
        return True

        

        