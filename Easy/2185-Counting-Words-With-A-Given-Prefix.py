class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_len = len(pref)
        count = 0
        
        for word in words:
            if word[:prefix_len] == pref:
                count += 1

        return count
        
