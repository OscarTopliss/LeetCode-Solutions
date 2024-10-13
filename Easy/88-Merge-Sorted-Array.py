class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range (m + n):
            if nums2 == []:
                continue

            if nums2[0] < nums1[x]:
                nums1.insert(x, nums2[0])
                nums2.pop(0)
                nums1.pop(-1)
                continue

            nums2_used_items = n - len(nums2)

            if x >= m + nums2_used_items:
                nums1.insert(x, nums2[0])
                nums2.pop(0)
                nums1.pop(x + 1)
