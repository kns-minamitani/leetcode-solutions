class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        w = int(sqrt(area))
        while area % w != 0:
            w -= 1
        l = area // w
        return [l, w]