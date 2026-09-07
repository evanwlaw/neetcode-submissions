class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Input: nums = [1,2,3,2,2]
        Output: 2


        Bruteforce: 
        - Nested loops to find dupe.
        - Time is O(N^2) and Space is still O(1) -> Valid
        
        We can see that this pretty trying to find cycles.
        See each nums[i] as ptr to next index

         0 1 2 3 4
        [1,2,3,2,2]

        i = 0 -> go to idx 1
        i = 1 -> go to idx 2
        i = 2 -> go to idx 3
        i = 3 -> go to idx 2
        i = 2 -> go to idx 3
        ..
        ..
        ..
        We see that we found a cycle.

        Using floyd's algo, we can find the start of the cycle which is the repeated number.


        Floyds:
        use two ptrs, slow and fast. First have them iterate until they meet this means there is a cycle.

        Then reset one of them to start.

        Then increment both ptrs by 1 until they meet. This is the repeated number.

        """
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0

        while True:
            slow, fast = nums[slow], nums[fast]

            if slow == fast:
                return slow
        


