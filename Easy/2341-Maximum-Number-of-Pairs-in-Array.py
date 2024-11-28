class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        seen = {}
        pairs = 0


        for num in nums:
            x = seen.setdefault(num, 0)
            seen[num] += 1

        for key in seen:
            pairs += seen[key] // 2
        
        return [pairs, len(nums) - (pairs * 2)]

        
