class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            ilen = len(words[i])
            iword = words[i]
            for j in range(i + 1, len(words)):
                jword = words[j]
                if jword[0 - ilen:] == iword and jword[:ilen] == iword:
                    count += 1
                    print(f"iword: {iword} jword: {jword}")
        
        return count
