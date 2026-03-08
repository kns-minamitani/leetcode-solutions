class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])
        result = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                total = 0
                count = 0

                for nr in range(r-1, r+2):
                    for nc in range(c-1, c+2):
                        if (0 <= nr < rows) and (0 <= nc < columns):
                            total += img[nr][nc]
                            count += 1
                result[r][c] = total // count

        return result