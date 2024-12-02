class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = [x for x in nums]

        for x in range(len(nums)):
            length = len(nums_copy)
            k = k % length
            index = (x - k)
            print(index)
            nums[x] = nums_copy[index]
