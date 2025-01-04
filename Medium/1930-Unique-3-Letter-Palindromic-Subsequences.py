class Solution:
    def isSubsequence(self, subsequence: str, s: str):
        sub_index = 0

        for letter in s:
            if letter == subsequence[sub_index]:
                if sub_index == 2:
                    return True
                sub_index += 1
        return False
        
        return False
        
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set()
        for letter in s:
            chars.add(letter)

        possible_subsequences  = [''.join(x) for x in itertools.product(list(chars), repeat = 3)
         if x[0] == x[2]]
        print(possible_subsequences)
        total = 0
        for subseq in possible_subsequences:
            
            if self.isSubsequence(subseq, s):
                print(subseq)
                total += 1
        
        return total
    
    


        
