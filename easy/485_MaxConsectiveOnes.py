class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consective = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif count > consective:
                consective = count
                count = 0
            else:
                count = 0
        return max(consective, count)