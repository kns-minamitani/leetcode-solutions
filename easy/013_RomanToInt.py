class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }
        Arabic = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and Roman[s[i]] < Roman[s[i+1]]:
                Arabic += Roman[s[i+1]] - Roman[s[i]]
                i += 2
            else:
                Arabic += Roman[s[i]]
                i += 1
        return Arabic