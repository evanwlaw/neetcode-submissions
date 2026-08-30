class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Input: nums = [1,2,1,0,4,2,6], k = 3
        Output: [2,2,4,4,6]
        

        iterate through nums until nums[k-1]
            we know the max up to now is 2 -> add to output
            if we move window by one,
            - we dont know if the value we drop at nums[i-k-1] is the max
            - we dont know if the value we add at nums[i+1] is the new max
        
        move window by 1 -> [1 : k + 1]
            we know the max up to now is still 2. - add to output
            we know the 0 added is not the new max.
            if we move window by one,
            - we dont know if the value we drop at nums[i-k-1] is the max
            - we dont know if the value we add at nums[i+1] is the new max
        
        move window by 1 -> [2 : k + 2]
            we know the max up to now is 4. - add to output
            we know the 4 added is the new max.
            we drop previous max, 2.
            if we move window by one,
            - we dont know if the value we drop at nums[i-k-1] is the max
            - we dont know if the value we add at nums[i+1] is the new max

        looks like we have a queue for the window. we drop far left and add far right each time. 

        We can make the window of the queue a max heap, and get the max to put into the output each time we move the window.

        This wouldnt be efficient as we need to make a new heap each time but it is brute force

        deque approach -> deque holds idx

        on each slide
            1. pop from back while right end of deque[-1] < than nums[i]
            2. add new idx to end
            3. popleft if the idx value is < i - k (start of window)
            4. add to output the first val of deque (front is always largest)

        nums = [1,2,1,0,4,2,6], k = 3

        i = 0 -> nums[0] = 1
        max is nums[0] -> 1, dont add to output yet
        deque = [0]

        i = 1 -> nums[1] = 2
        max -> nums[1] -> 2, dont add ot output yet
        deque = [1]

        i = 2 -> nums[2] = 1
        max is nums[1] -> 2, add deque[0] to output
        deque = [1]

        Start sliding here:

        i = 3 -> nums[3] = 0
        check if nums[deque[-1]] < nums[i] -> no
        deque = [1]
        check if deque[0] < 3 - 3 + 1 (i - k + 1) -> no
        output.append(nums[deque[0]])
        output[2]

        i = 4 -> nums[4] = 4
        check if nums[deque[-1]] < nums[i] -> yes. popright
        deque = [4]
        check if deque[0] < 4 - 3 + 1 (i - k + 1) -> no
        output.append(nums[deque[0]])
        output[2, 4]
        """
        output = []
        queue = deque()

        for i in range(len(nums)):
          
            # during slide
            # 1. while nums[deque[-1]] < nums[i], pop right from deque
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            # 2. Append i to deque
            queue.append(i)

            # 3. check if deque[0] in out of bounds < i - k + 1. popleft is so
            while queue[0] < (i - k + 1):
                queue.popleft()
            # 4. append max to output
            if queue and i >= k - 1:
                output.append(nums[queue[0]])
        return output

