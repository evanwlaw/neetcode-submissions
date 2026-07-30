class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Create key via counts of of the word.

        acts -> [101....00]
        cat ->

        '''
        output = defaultdict(list) # [count] : anagram list

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            output[tuple(count)].append(s)
        return list(output.values())