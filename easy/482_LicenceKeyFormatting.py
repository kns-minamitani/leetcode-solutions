class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        result = []
        i = len(s)
        while i > 0:
            result.append(s[max(0, i-k): i])
            i -= k
        return '-'.join(reversed(result))