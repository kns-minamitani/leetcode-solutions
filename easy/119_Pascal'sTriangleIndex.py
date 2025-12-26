class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            result[i] = int(math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex - i)))
        return result
