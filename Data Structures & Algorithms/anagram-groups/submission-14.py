class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        freq = {}

        [(001023... ): [a1,a2,...]]
        
        # each str, get count and append itself to that count

        # return list(dict.values())

        """
        freq = defaultdict(list)
        
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            freq[tuple(counts)].append(s)
        return list(freq.values())
