class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        s_index = 0
        if s_length == 0:
            return True
        for character in t:
            if character == s[s_index]:
                s_index = s_index + 1
                if s_index == s_length:
                    return True
        return False
        
