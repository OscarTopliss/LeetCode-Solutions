class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            if len([x for x in words if word in x]) != 1:
                output.append(word)
        
        return output
