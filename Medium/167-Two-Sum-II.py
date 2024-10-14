class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Find earliest positive number
       
        earliest_positive_index = 0

        for index in range(len(numbers)):
            if numbers[index] >= 0:
                earliest_positive_index = index
                break
        
        if target < 0:
            for index in range(earliest_positive_index):
                for index2 in range(len(numbers)):
                    if numbers[index] + numbers[index2] == target and index != index2:
                        return [index + 1, index2 + 1]

        if target >= 0:
            for index in range(earliest_positive_index, len(numbers)):
                if index > 0:
                    if numbers[index] == numbers[index - 1]:
                        continue
                for index2 in range(len(numbers)):
                    if numbers[index] + numbers[index2] == target and index != index2:
                        if index2 < index:
                            return [index2 + 1, index + 1]
                        return [index + 1, index2 + 1]
