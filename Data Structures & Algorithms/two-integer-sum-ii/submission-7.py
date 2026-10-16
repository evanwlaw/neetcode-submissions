class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        looks liek two sum
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            checkSum = numbers[l] + numbers[r]
            if checkSum == target:
                return [l + 1, r + 1]
            
            if checkSum < target:
                l += 1
            else:
                r -= 1
        