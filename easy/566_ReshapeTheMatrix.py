class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]
        
        for idx in range(m * n):
            result[idx//c][idx%c] = mat[idx//n][idx%n]
        return result