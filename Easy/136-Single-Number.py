class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for x in range(1, len(nums)):
            xor = xor ^ nums[x]
        return xor
