class Solution:
    def isHappy(self, n: int) -> bool:
        memory = []
        while n**2 > 9 and n not in memory:
            strings = str(n)
            ans = 0
            for i in range(len(strings)):
                ans += int(strings[i])**2
            memory.append(n)
            n = ans
        if n == 1:
            return True
        else:
            return False