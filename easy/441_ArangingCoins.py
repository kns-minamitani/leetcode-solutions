class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins = (mid * (mid+1)) // 2
            if coins < n:
                left = mid + 1
            elif coins > n:
                right = mid - 1
            else:
                return mid
        return right