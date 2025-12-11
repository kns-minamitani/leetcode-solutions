class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_sub = len(haystack) - len(needle)
        for i in range(len_sub+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1