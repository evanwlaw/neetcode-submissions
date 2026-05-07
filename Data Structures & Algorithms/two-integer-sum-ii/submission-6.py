class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            check = numbers[l] + numbers[r]

            if check < target:
                l += 1
            elif check > target:
                r -= 1
            else:
                return [l + 1, r + 1]