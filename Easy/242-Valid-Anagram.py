class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        for x in s:
            if s.count(x) == t.count(x):
                s = s.replace(x, "")
                t = t.replace(x, "")
            else:
                return False
        if s == "" and t == "":
            return True
        return False
