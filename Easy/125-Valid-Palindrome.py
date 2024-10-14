class Solution:
    def isPalindrome(self, s: str) -> bool:
        givenString = s
        givenString = givenString.lower()

        
        cleaned_string = ""
        # Remove non-alphanumeric characters
        for letter in givenString:
            if letter.isalnum():
                cleaned_string = cleaned_string + letter
            
        for index in range (len(cleaned_string)//2):
            if cleaned_string[index] != cleaned_string[-1 - index]:
                return False
        
        return True
