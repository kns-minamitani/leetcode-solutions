class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False 
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        letters = {}
        for i in magazine:
            letters[i] = letters.get(i, 0) + 1
        for j in ransomNote:
            if j in letters and letters[j] != 1:
                letters[j] -= 1
            elif j in letters and letters[j] == 1:
                del letters[j]
            else:
                return False
        return True