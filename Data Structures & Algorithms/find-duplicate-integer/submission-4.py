class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        0   1   2   3   4  

        1   2   3   2   2

        range is 1:n. can think of each value a ptr. 
        index is the node. value is ptr to next

        guarantee 0 node is not in cycle -> duplicate = cycle
        use floyd's of slow and fast ptrs

        run 1 time to identify cycle.
        run 2, reset 1 fast/slow ptr to find the beginning


        """

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return fast
            
            