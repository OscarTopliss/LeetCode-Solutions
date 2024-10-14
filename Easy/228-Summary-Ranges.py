class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        
        ranges = []

        if nums == []:
            return ranges
        
        if len(nums) == 1:
            ranges.append(str(nums[0]))
            return ranges

        smallest_number = nums[0]
        largest_number = None

        

        for x in range(len(nums) - 1):
            if nums[x] + 1 == nums[x + 1]:
                largest_number = nums[x + 1]
                continue
            if largest_number == None:
                new_range = str(smallest_number)
                ranges.append(new_range)
                smallest_number = nums[x + 1]
                continue
            new_range = str(smallest_number) + "->" + str(largest_number)
            ranges.append(new_range)
            largest_number = None
            smallest_number = nums[x + 1]
        
        final_number_index = len(nums) - 1

        if largest_number == None:
            new_range = str(nums[final_number_index])
            ranges.append(new_range)
        else:
            new_range = str(smallest_number) + "->" + str(nums[final_number_index])
            ranges.append(new_range)

        
        return ranges
