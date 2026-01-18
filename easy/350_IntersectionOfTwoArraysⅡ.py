class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        e_nums1 = {}
        result = []
        for i in nums1:
            e_nums1[i] = e_nums1.get(i, 0) + 1
        for j in nums2:
            if j in e_nums1:
                e_nums1[j] -= 1
                result.append(j)
                if e_nums1[j] == 0:
                    del e_nums1[j]
        return result