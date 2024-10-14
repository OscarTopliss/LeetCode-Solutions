class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        for index in range(len(numbers) - 1):
            try:
                index_2 = numbers.index(target - numbers[index], index + 1)
                return [index + 1, index_2 + 1] 
            except ValueError:
                continue
