class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType) // 2
        types = len(set(candyType))

        return min(limit, types)