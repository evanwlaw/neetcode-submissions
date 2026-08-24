class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [2,-1,1,2], k = 2
        Output: 4

        iterating through nums[0] -> 2
        this equals to k. if we move on, we don't know if this nums[0] can be used later for another subarray. 

        iterating through nums[1] -> -1
        this equals to k - 3. if we move on, we don't know if this nums[1] can be used later for another subarray.
        
        iterating through nums[2] -> 1
        this equals to k - 1. if we move on, we don't know if this nums[2] can be used later for another subarray or was part of one. And it is, nums[2], nums[1], nums[0] all add up to k.  
        
        
        Looks like we may need to keep a running total sum as a variable
        And hashmap where key is the sum : value is number of times seen

        """

        running_total = 0
        hash_map = {0:1} # sum : freq
        output = 0

        for n in nums:
            running_total += n

            # running_total - k -> prev sum
            prev_sum = running_total - k
            if prev_sum in hash_map:
                output += hash_map[prev_sum]
            hash_map[running_total] = 1 + hash_map.get(running_total,0)
        return output


