class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: nums = [1,2,2,3,3,3,3], k = 2

        Step 1: create freq map
        freq_map = {} num:occ
        {1:1, 3:4, 2:2}

        Step 2: put into freq list
        freq_list = [[] for _ in range(len() + 1)


        Step 3: iterate backwards in freq_list to get res until k
        """

        freq_map = {}

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        
        freq_list = [[] for _ in range(len(nums) + 1)]

        for n, i in freq_map.items():
            freq_list[i].append(n)
        
        res = []
        for i in range(len(freq_list) - 1, -1, -1):
            
            for j in freq_list[i]:
                res.append(j)
                if len(res) >= k:
                    return res



