class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        number_dict = {}
        for num in arr:
            number_dict.setdefault(num, 0)
            number_dict[num] += 1
        
        for num in arr:
            if num * 2 in number_dict:
                if num != 0:
                    return True
                if number_dict[num] > 1:
                    return True
        
        return False
