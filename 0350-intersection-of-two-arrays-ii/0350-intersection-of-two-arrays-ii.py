class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for n in nums2:
            if n in nums1:
                result.append(n)
                nums1.remove(n)

        return result
