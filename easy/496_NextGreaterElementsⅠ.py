class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums2 = {}
        for j, x in enumerate(nums2):
            dict_nums2[x] = j
        result = []
        for i in range(len(nums1)):
            j = dict_nums2[nums1[i]]
            while j < len(nums2) and nums2[j] <= nums1[i]:
                j += 1
            if j >= len(nums2):
                result.append(-1)
            else:
                result.append(nums2[j])
        return result