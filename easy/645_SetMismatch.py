class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup = -1
        for i in nums:
            if i in seen:
                dup = i
            else:
                seen.add(i)
        
        for j in range(1, len(nums)+1):
            if j not in seen:
                return [dup, j]