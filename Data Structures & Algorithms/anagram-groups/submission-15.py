class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Input: list of strings. 
        Output: list of sublists that contain, all anagrams.

        Idea: Use a hashmap to group anagrams together. The key is a character frequency array of size 26 where each element is the number of times it appears in the string.
                a      e    ut
        eat -> [10001...01]
        tea -> [10001...01]

        The value of the hashmap is a list of the anagrams. so  [10001...01] : ["eat", "tea"]

        For each string in the input:
            get the character frequency key of each string -> go through each character to get the mapping (ord(c) - ord('a'))
        then append the string to values at the frequency key -> hashmap[character_frequency].append(string)
        return in list the values in the hashmap

        Time Complexity: O(n) - we iterate through the input list of length n. We need to go through char of each string so it would be O(m * n) where m is the len of the longest string. This is simplified to O(n)
        Space Complexity: O(n) - need to store all items in the input to the hashmap, so O(n) is the worst case.

        Time to solve problem:

        '''

        frequency_map = defaultdict(list) # char_frequency : [a1, a2,...]

        for s in strs:
            char_frequency = [0] * 26
            for c in s:
                char_frequency[ord(c) - ord('a')] += 1

            # need to change char_frequency into immutable tuple to work as a key
            frequency_map[tuple(char_frequency)].append(s)
        return list(frequency_map.values())
