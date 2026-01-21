class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for x in s:
            letters[x] = letters.get(x, 0) + 1
        for y in t:
            if y not in letters:
                return y
            letters[y] -= 1
            if letters[y] == 0:
                del letters[y]
        