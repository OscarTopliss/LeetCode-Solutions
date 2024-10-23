class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ['(','{','[']:
                stack.append(character)
            
            if character in [')','}',']']:
                if len(stack) == 0:
                    return False
                if character == ')' and stack[-1] != '(':
                    return False
                if character == '}' and stack[-1] != '{':
                    return False
                if character == ']' and stack[-1] != '[':
                    return False
                stack.pop(-1)

        if len(stack) != 0:
            return False
        return True
        
