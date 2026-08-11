class Solution:
    """
    Find the total count of continuous subarrays whose elements sum up to a target integer k.

    Input: nums = [1, 1, 1], k = 2
    Output: 2

    Input: nums = [1,2,3], k = 3
    Output: 2
    """

    """
    [1   1   1]         k = 2 -> 2

    [1   2   3]         k = 3 -> 2

    [1   8   3   2]         k = 3 -> 1

    map[9] -> 1
    map[12] -> 12 - 3 = 9 -> exists in map -> add map[9] to output
    map[14] -> 14 - 3 = 11 -> doesnt exist in map -> add map[14] = 1 + map.get(14, 0)

    Brute force -> iterate with nested loops see if sum equals k.
    Better way is to see if we get prev calculated subarrays instead repetively summing.

    Track the subarrays -> need a way to retrieve previously calculated sums
    Use a hashmap.

    running_total + prev_calc = k -> running_total - k = prev_calc
    See if prev_calc exists in hashmap -> if so, it means we can remove 

    Time Complexity: O(N) - We run through the input nums list just once and perform O(1) operations to find all the subarrays if they exist. So the time complexity is O(N)
    Space Complexity: O(N) - Space is used to hold the running total sums which is up to N-1 key/value pairs. Therefore, space complexity is O(N)
    Time Spent on Problem: 20 minutes
    """
    def subarraySum(self, nums: list[int], k: int) -> int:
        h_map = {0 : 1}
        output = 0
        running_total = 0

        for n in nums:
            running_total += n
            prev_calc = running_total - k

            if prev_calc in h_map:
                output += h_map.get(prev_calc, 0)

            h_map[running_total] = 1 + h_map.get(running_total, 0)
        return output

