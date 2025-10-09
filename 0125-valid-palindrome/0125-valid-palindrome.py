class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for sub in s:
            if sub.isalnum():
                strs.append(sub.lower())

        return strs == strs[::-1]