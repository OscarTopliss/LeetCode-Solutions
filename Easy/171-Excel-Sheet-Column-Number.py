class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        columnNum = 0

        columnTitle_rev = columnTitle[::-1]

        for x in range(len(columnTitle_rev)):
            columnNum += (26 ** x) * (alphabet.index(columnTitle_rev[x]) + 1)
        
        return columnNum
