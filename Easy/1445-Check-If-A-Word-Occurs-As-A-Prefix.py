class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        prefix_len = len(searchWord)
        words = sentence.split(" ")

        for x in range(len(words)):
            if words[x][:prefix_len] == searchWord:
                return x + 1
        
        return -1
        
