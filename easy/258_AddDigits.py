class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            str_num = str(num)
            num = 0
            for i in str_num:
                num += int(i)
        return num