class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1 : 1
        2 : 2
        3 : 3

        0   1   2   3
        """

        freq = {}

        for c in nums:
            freq[c] = 1 + freq.get(c, 0)

        freq_array = [[] for _ in range(len(nums) + 1)]

        for v, i in freq.items():
            freq_array[i].append(v)
        
        res = []
        for i in range(len(freq_array) - 1, -1, -1):
            for j in freq_array[i]:
                res.append(j)
                if len(res) == k:
                    return res
            


