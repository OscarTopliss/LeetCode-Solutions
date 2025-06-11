class Solution:
    def romanToInt(self, s: str) -> int:
        numeral = s
        total = 0
        while len(numeral) > 0:
            result = self.parseComponent(numeral)
            numeral = result[1]
            total += result[0]

        return total


    def parseComponent(self, numeral: str):
        if numeral[0] == "M":
            return (1000, numeral[1:])

        if numeral [0] == "D":
            return (500, numeral[1:])

        if numeral[0] == "C":

            if len(numeral) > 1 and numeral[1] == "M":
                return (900, numeral[2:])

            if len(numeral) > 1 and numeral[1] == "D":
                return (400, numeral[2:])
            
            return (100, numeral[1:])

        if numeral[0] == "L":
            return (50, numeral[1:])
        
        if numeral[0] == "X":

            if len(numeral) > 1 and numeral[1] == "C":
                return (90, numeral[2:])

            if len(numeral) > 1 and numeral[1] == "L":
                return (40, numeral[2:])
            
            return (10, numeral[1:])

        if numeral[0] == "V":
            return (5, numeral[1:])

        if numeral [0] == "I":

            if len(numeral) > 1 and numeral[1] == "X":
                return (9, numeral[2:])

            if len(numeral) > 1 and numeral[1] == "V":
                return (4, numeral[2:])

            return (1, numeral[1:])
