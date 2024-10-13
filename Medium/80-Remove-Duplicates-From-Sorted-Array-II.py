class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        while index < len(nums) - 1:
            if nums[index - 1] == nums[index + 1]:
                nums.pop(index)
                continue
            index = index + 1

        
