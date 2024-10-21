class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for x in range(1, len(s) + 1):
            if s[-x] == " " and length == 0:
                continue
            if s[-x] == " ":
                return length
            length += 1
        return length
