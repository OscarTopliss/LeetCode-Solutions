class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}
        for letter in magazine:
            if letter not in magazine_letters:
                magazine_letters[letter] = 1
                continue
            magazine_letters[letter] += 1
        
        for letter in ransomNote:
            if letter not in magazine_letters:
                return False
            if magazine_letters[letter] == 0:
                return False
            magazine_letters[letter] -= 1

        return True

        
