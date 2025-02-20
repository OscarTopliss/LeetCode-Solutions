class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aval = 0
        bval = 0

        a_rev = a[::-1]
        b_rev = b[::-1]

        for x in range(len(a_rev)):
            if a_rev[x] == "1":
                aval += 2 ** x
        
        for x in range(len(b_rev)):
            if b_rev[x] == "1":
                bval += 2 ** x
        
        total = aval + bval

        return format(total, 'b')
        
