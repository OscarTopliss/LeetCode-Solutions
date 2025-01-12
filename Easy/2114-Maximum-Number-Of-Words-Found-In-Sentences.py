class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        largest_num = 0
        for sentence in sentences:
            largest_num = max(largest_num, len(sentence.split(' ')))
        
        return largest_num
