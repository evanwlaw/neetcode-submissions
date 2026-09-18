class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

        sort nums -> may help us skip over already processed

        -4  -1  -1  0   1   2

        start with -4
            then two ptrs at i + 1 and len(nums) -1 -> l and r

            get their sum at nums[i] + nums[l] + nums[r]
                if sum < 0:
                    move l
                elif sum > 0:
                    move r
                else: we found 0
                    output.append([nums[i], nums[l], nums[r]])

                    there might be still triples at this current i, but we want to skip potentially seen ones.
                    increment l once, and if nums[l] == nums[l-1] then keep incrementing
                    

        """
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1 
            
            while l < r:
                check_sum = nums[i] + nums[l] + nums[r]

                if check_sum < 0:
                    l += 1
                elif check_sum > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output
