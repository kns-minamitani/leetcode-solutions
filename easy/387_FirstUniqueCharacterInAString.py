class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        letters = set()
        for i in range(len(s)-1):
            if s[i] not in letters and s[i] not in set(s[i+1:]):
                return i
            letters.add(s[i])
        if s[-1] not in letters:
            return len(s)-1
        return -1