class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        input: array of unsorted numbers
        output: array of triplets. A triplet is made of the 3 elements whose sum equals 0. Must not have duplicate triplets. [-1,-1,2] is the same as [-1,2,-1] and these would append one and not two.

        -4	-1	-1	0 	1	2
        i
            l
                            r
        Idea: sort input array. Use 3 ptrs (e.g. i, l, and r). Iterate through input via i. Find if the sum of elements are i, l, r sum to 0. If sum is < or > than 0, move ptrs l and r respectively. (basically, iterate through input and solve two sum on each element of input)

        Sort input in place.
        Iterate through input via ptr i.
        Continue to loop if i > 0 and if current element at i == element at i - 1 
        Setup ptr l starting i + 1 and ptr r at the end of the input array.
        iterate while l < r:
        Move l if sum < 0.
        Move r if sum > 0.
        Add the elements at i, l, r to the output array.
            Need to update ptr l -> make sure it’s not the same one as previous l (skips duplicates) 
        Return output list

        Time complexity: O(N*logN ) - sorting algorithm would take O(N*logN). We’re running through the input array once with while loops skipping over duplicate values which is O(N). The worst case time of the sort dominates, so O(N*logN).
        Space Complexity: O(N) - Sorting in place so no new space is used for that. Only extra space used is for the pointers for the output which would take O(N/3) worst case which simplifies to O(N).
        '''
        output = []
        if len(nums) < 3: # return empty list if input is invalid 
            return output
        n = len(nums) - 1
        nums.sort()
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n
            while l < r:
                check_sum = nums[i] + nums[l] + nums[r]
                
                if check_sum < 0:
                    l += 1
                elif check_sum > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    # make sure we skip duplicates at l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return output
