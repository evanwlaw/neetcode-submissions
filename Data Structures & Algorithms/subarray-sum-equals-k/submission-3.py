class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Iterate through nums
        Have a running total sum of what we've seen so far.

        t_sum - prev_slice = k -> prev_slice = t_sum - k

        Have prev_slice sum values in map
        freq -> {sum_val : num of times seen}

        if prev_slice in freq -> output += freq[prev_slice]
        """
        freq = {0: 1} # val : count
        output = 0
        t_sum = 0

        for n in nums:
            t_sum += n
            prev_slice = t_sum - k

            if prev_slice in freq:
            # add if seen before. even if never seen before, 0 will be added
                output += freq[prev_slice]
            freq[t_sum] = 1 + freq.get(t_sum, 0)
        return output
