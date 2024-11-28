class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        if 0 in seen:
            return len(seen) 0
        return len(seen)
