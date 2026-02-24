class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occuerence = {letter: i for i, letter in enumerate(s)}

        seen = set()
        for i, letter in enumerate(s):
            if  letter not in seen:
                while stack and stack[-1] > letter and last_occuerence[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(letter)
                stack.append(letter)
        return ''.join(stack)