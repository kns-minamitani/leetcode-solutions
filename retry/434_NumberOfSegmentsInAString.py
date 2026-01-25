class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        in_word = False
        for char in s:
            if char != ' ':
                if not in_word:
                    segments += 1
                    in_word = True
            else:
                in_word = False
        return segments
