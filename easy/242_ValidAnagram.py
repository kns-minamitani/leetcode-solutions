class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for i in s:
            letters[i] = letters.get(i, 0) + 1
        for j in t:
            if j not in letters:
                return False
            else:
                letters[j] -= 1
            if letters[j] == 0:
                del letters[j]
    
        return not letters
