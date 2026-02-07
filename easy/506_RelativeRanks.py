class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        if n == 1:
            return ["Gold Medal"]
        record = {}
        for i, x in enumerate(score):
            record[x] = i
        score.sort()
        result = [0] * n
        if n == 2:
            result[record[score[0]]] = "Silver Medal"
            result[record[score[1]]] = "Gold Medal"
            return result
        j = 0
        while n > 3:
            result[record[score[j]]] = str(n)
            j += 1
            n -= 1
        result[record[score[j]]] = "Bronze Medal"
        result[record[score[j+1]]] = "Silver Medal"
        result[record[score[j+2]]] = "Gold Medal"
        return result