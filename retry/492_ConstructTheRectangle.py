class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        left, right = 1, area
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == area:
                w = mid
                break
            elif sq < area:
                left = mid + 1
            else:
                right = mid - 1
        else:
            w = right
        
        while area % w != 0:
            w -= 1
        
        return [area//w, w]