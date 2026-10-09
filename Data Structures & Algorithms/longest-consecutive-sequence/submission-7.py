class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        so bc of O(n) time, we can't sort with an algo of O(nlogn)

        goal: return the len of the longest consecutive sequence (e.g. 1,2,3,4 -> 4)

        Input: nums = [0,3,2,5,4,6,1,1]
        Output: 7 -> 0,1,2,3,4,5,6

        we need to know:
        1. how to find the first number in a sequence
        2. if the next number in sequence -> exists?

        we dont care about duplicates

        1. we can use a set to hold each nums[i] (skips dupes) -> O(n) time
        2. iterate through nums
            if nums[i] - 1 not set -> first number in sequence
                currLen = 1

                while currLen < len(nums) and nums[i] + currLen in set:
                    currLen += 1
                
                maxArea = max(currLen, maxArea)

        2, 20, 4, 10, 3, 4, 5 -> return 4 (2,3,4,5)
        1. set -> 2, 20, 4, 10, 3, 4, 5
        2. iterate
            2 -> sequence start
                since currLen == 1 and 2 + currLen (3) in set -> currLen = 2
            3 -> next num
                since currLen == 2 and 3 + currLen (4) in set -> currLen = 3
            4 -> next num
                since currLen == 3 and 4 + currLen (5) in set -> currLen = 4
            5 -> next num
                since currLen == 4 and 5 + currLen (6) in NOT in set -> terminate while loop
            update maxArea to 4
            since next nums[i] -> 20 is a start of sequence, we go into loop. but len is 1 so no updates. 
            next nums[i] is 4, it's not the first so continue
            ..
            ..
            return maxArea

        Time: O(n) - O(n) time to setup set + for loop is also O(n). we dont check non start values and only the start values -> worst case is O(n)
        Space: O(n) - worst case is that every number is unique in input nums
        """

        maxArea = 0
        numSet = set()
        for n in nums:
            numSet.add(n)
        
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                currLen = 1

                while currLen < len(nums) and nums[i] + currLen in numSet:
                    currLen += 1
                maxArea = max(maxArea, currLen)
        return maxArea


