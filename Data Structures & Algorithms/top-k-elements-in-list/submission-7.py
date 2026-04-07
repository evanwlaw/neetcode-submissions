class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        get a dictionary of counts
        count dict {v:occ}
        1:1, 2:2, 3:3, 4:3

        then have a frequency list where idx is the number of occ
        freq[v] = count.get(v,0)

        freq list:
        0   1   2   3   4   5   6
            [1]   [2]   [3,4]
        """

        count = {} # v: occ
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for v, c in count.items():
            freq[c].append(v)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    

        