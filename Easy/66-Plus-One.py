class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        while index >= 0 - len(digits):
            if digits[index] != 9:
                digits[index] += 1
                break
            digits[index] = 0
            if digits[index] == digits[0]:
                digits.insert(0, 1)
                break
            index -= 1
        return digits
        
