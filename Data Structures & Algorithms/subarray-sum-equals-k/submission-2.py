class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        res = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n
            check = curr_sum - k

            res += freq.get(check, 0)
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        return res