class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            minimum = len(word1)
            min_word = "word1"
        else:
            minimum = len(word2)
            min_word = "word2"

        combined_string = ""
        
        for x in range(minimum):
            combined_string += word1[x]
            combined_string += word2[x]

        if len(word1) == len(word2):
            print("1")
            return combined_string
        
        if min_word == "word1":
            combined_string += word2[minimum:]
            return combined_string
        
        if min_word == "word2":
            combined_string += word1[minimum:]
            return combined_string
