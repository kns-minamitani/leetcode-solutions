class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words = {}
        for i, x in enumerate(list1):
            words[x] = i
        best = float('inf')
        result = []

        for j, y in enumerate(list2):
            if y in words:
                order = j + words[y]
                if order < best:
                    best = order
                    result = [y]
                elif order == best:
                    result.append(y)
        
        return result