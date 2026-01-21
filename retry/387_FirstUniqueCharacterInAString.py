class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for x in s:
            letters[x] = letters.get(x, 0) + 1
        for i, x in enumerate(s):
            if letters[x] == 1:
                return i
        return -1