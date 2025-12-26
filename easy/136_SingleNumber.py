class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = set()
        not_first = set()
        for i in nums:
            if i not in first:
                first.add(i)
            else:
                not_first.add(i)
        return list(first - not_first)[0]