class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums)):
            # 連続していない場合
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start = nums[i]

        # 最後の区間を追加
        end = nums[-1]
        if start == end:
            res.append(str(start))
        else:
            res.append(f"{start}->{end}")

        return res