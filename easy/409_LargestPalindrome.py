class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        length = 0
        has_odd = False

        for v in cnt.values():
            length += (v // 2) * 2
            if v % 2 == 1:
                has_odd = True

        return length + (1 if has_odd else 0)