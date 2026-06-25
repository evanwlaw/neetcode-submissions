class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Input: Array of ints. And k, the number elements to return
        Output: Array of the top k elements.

        Idea: Time needs to be more than O(n log n) signals to me that we cannot sort. Use a hashmap of the element as the key and value as the frequency it occurs in the input.

        First step: populate a hashmap with elements and their frequencies.

        Second step: Populate an array of len(input) + 1 where the indices are the frequencies (worst case is there is only 1 element that is repeated in input). Append elements as sublists. This sorts our hashmap linearly into an array based on the frequency
        0	1	2	3	4	5	6
                [3]	[2]	[1]

        Third step: Iterate backwards through the frequency array we just sorted. Need to iterate through each sublist and append to an output array. If len(output) == k, we return the output.

        Time Complexity: O(n) - We iterate through the input array to populate hashmap, which is O(n) time. And then iterating through the hashmap is O(m) where m is the number of unique elements in the input to sort elements into an array. And finally, iterating through the array is O(n) where in the worst case we need to go through entirely. This is O(n + m + n) which simplifies to just O(n) 
        Space Complexity: O(n) - Hashmap will take O(m) where m is the number of unique elements in the input. And then the array to hold frequencies will take O(n + 1) space due to the case where every element is the same. O(n + 1) is the dominating one which simplifies to O(n)

        Time to solve problem: 25 minutes
        '''
        freq_map = {} # number : frequency

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)

        freq_array = [[] for _ in range(len(nums) + 1) ]
        for n, i in freq_map.items():
            freq_array[i].append(n)

        output = []
        for i in range(len(freq_array) -1, -1, -1):
            for j in freq_array[i]:
                output.append(j)
                if len(output) == k:
                    return output
        return -1 # if we're here, it means input is invalid e.g. number of unique elements < k
