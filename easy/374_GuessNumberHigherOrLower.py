# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            num = (left + right) // 2
            h_or_l = guess(num)
            if h_or_l == 0:
                return num
            elif h_or_l == 1:
                left = num + 1
            else:
                right = num - 1