class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(len(result)):
            con = 0
            j = i
            while j > 0:
                con += j % 2
                j //= 2
            result[i] = con
        return result