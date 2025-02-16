class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):

            remainder = target - nums[x]

            if remainder in nums[x+1:]:
                return [x, x + 1 + nums[x+1:].index(remainder)]
