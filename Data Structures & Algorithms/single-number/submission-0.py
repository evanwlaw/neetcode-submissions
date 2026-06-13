class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        0 : []
        1 : []
        2 : []

        iterate through nums:
            if hash[]

        """ 
        freq = {1:[], 2:[]}

        for n in nums:
            if n in freq[1]:
                freq[1].remove(n)
                freq[2].append(n)
            else:
                freq[1].append(n)
        
        return freq[1][0]
