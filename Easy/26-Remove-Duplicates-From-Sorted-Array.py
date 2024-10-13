class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            try:
                while nums[index] == nums[index + 1]:
                    nums.pop(index + 1)
            except IndexError:
                continue
            index = index + 1
        
        return len(nums)
