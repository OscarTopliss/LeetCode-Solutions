class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for x in range(1, len(strs[0]) + 1):
            try:
                if all(string[0:x] == strs[0][0:x] for string in strs):
                    prefix = strs[0][0:x]
                else:
                    return prefix
            except IndexError:
                return prefix

        return prefix
