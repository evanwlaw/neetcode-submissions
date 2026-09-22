class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Input: nums = [1,2,2,3,3,3], k = 2
        Output: [2,3]

        get all counts of each number into a hashmap
        hashmap -> num : freq
        1 : 1
        2 : 2
        3 : 3

        Then put into a frequency array of size len(nums).
        Each idx of freq is the number of times it appears in
    

        freq 
        i    0   1   2   3   4   5   6
        v        1   2   3

        then run backwards from freq until output list is len(k)
        """

        freq_map = {}

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        
        freq_array = [[] for _ in range(len(nums) + 1) ]

        for num, idx in freq_map.items():
            freq_array[idx].append(num)
        
        output = []
        for i in range(len(freq_array) - 1, -1, -1):
            for j in freq_array[i]:
                output.append(j)
                if len(output) == k:
                    return output
        return -1
