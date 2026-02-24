class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        ans = 0
        for j in count:
            if j+1 in count:
                ans = max(ans, count[j] + count[j+1])
        
        return ans