class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largestOnes = 0
        currentOnes = 0
        for num in nums:
            if num == 1:
                currentOnes += 1
            else:
                currentOnes = 0
                continue
            if currentOnes > largestOnes:
                largestOnes = currentOnes

        return largestOnes
