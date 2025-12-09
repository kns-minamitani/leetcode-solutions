class Solution:
    def climbStairs(self, n: int) -> int:
        way = []
        result = 1
        two = n//2
        if n%2 == 0:
            one = 0                 
        else:
            one = 1
        while two > 0:
            way.append(math.factorial(two + one)/(math.factorial(two) * math.factorial(one)))
            two -= 1
            one += 2
        for i in way:
            result += int(i)
        return result