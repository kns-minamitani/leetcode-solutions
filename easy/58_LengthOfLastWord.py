class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_margin = 0
        while s[-(last_margin+1)] == " ":
            last_margin += 1
        i = last_margin
        while i < len(s) and s[-(i+1)] != " ":
            i += 1
        last_word = i - last_margin
        return last_word
        