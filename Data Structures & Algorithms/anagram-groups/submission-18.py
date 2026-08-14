from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        anagram_map = defaultdict(list) # [count : [a1, a2,...]]

        for s in strs:
            freq_count = [0] * 26

            for c in s:
                freq_count[ord(c) - ord('a')] += 1

            anagram_map[tuple(freq_count)].append(s)

        return list(anagram_map.values())