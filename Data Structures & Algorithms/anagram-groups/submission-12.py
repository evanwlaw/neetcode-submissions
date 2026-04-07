class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input list of strs
        # output: list of sublists of anagrams (aka with same number of letter occurences)

        # use freq map
        # freq = {} [[010....0]: [anagram1, anagram2,...]]
        # use defaultdict for keys that dont exist
        # append each anagram to the count key (needs to be tuple)
        freq = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freq[tuple(count)].append(s)
            
        return list(freq.values())