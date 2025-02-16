class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return
        largest_len = 1

        start_index = 0
        end_index = 0

        for x in range(len(s)):
            end_index = x
            print(f"start_index:{start_index}\nend_index:{end_index}\ns[start_index:end_index + 1] = {s[start_index:end_index + 1]}\ns[start_index:end_index + 1].count(s[end_index]) = {s[start_index:end_index + 1].count(s[end_index])}\n")
            while s[start_index:end_index + 1].count(s[end_index]) > 1:
                start_index += 1

            cur_len = end_index - start_index + 1
            if cur_len > largest_len:
                largest_len = cur_len

        return largest_len
        
