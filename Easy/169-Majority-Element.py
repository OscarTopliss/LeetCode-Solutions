class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen_items = []
        seen_freqs = []

        for item in nums:
            if not item in seen_items:
                seen_items.append(item)
                seen_freqs.append(1)
                continue
            index = seen_items.index(item)
            seen_freqs[index] = seen_freqs[index] + 1

        current_item = None
        current_freq = 0
        for x in range(len(seen_freqs)):
            if seen_freqs[x] > current_freq:
                current_item = seen_items[x]
                current_freq = seen_freqs[x]

        return current_item
