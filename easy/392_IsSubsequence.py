class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        i = 0
        for c in t:
            if i < s_length and s[i] == c:
                i += 1
        return i == s_length