class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if format(n, 'b').count("1") == 1 and n > 0:
            return True
        return False
