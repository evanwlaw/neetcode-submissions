class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dictionary = {}          

        for n in nums:          
            my_dictionary[n] = 1 + my_dictionary.get(n, 0)    
                
        freq = [[] for _ in range(len(nums) + 1)]          

        for n, i in my_dictionary.items():          
            freq[i].append(n)    
            
        res = []          
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:          
                res.append(j)
                if len(res) >= k:
                    return res