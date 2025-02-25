class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for x in range(1, n + 1):
            if x % 15 == 0:
                output.append("FizzBuzz")
                continue
            if x % 3 == 0:
                output.append("Fizz")
                continue
            if x % 5 == 0:
                output.append("Buzz")
                continue
            output.append(str(x))

        return output
            
                
