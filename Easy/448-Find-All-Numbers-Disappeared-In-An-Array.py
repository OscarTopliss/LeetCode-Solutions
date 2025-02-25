class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maximum = len(nums)
        nums_set = set(nums)
        # using a hash set gives O(1) search for "if x not in" vs O(n) search for a list
        missing = []

        for x in range(1, maximum + 1):
            if x not in nums_set:
                missing.append(x)
        
        return missing
            
