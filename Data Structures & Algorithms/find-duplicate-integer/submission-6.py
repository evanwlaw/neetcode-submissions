class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        

    idx 0   1   2   3   4
    val 1   2   3   2   2

        0 -> 1 -> 2 -> 3 -> 2 -> 3 -> 2 ->,....

        Use floyd's algorithm to detect cycle start
            - detect cycle
            - find start of cycle
        """

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # at this point, we found a cycle where pointers meet
        # reset one of the points to 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow


