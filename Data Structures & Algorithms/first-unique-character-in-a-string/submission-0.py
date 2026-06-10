class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Naive solution: use two nested loops to compare if s[i] does not repeat with s[j]. If there is a repeating char between s[i] and s[j] then continue to next s[i]. This will take O(n^2) time in worst case.

        A better solution would be to use a hashmap to track which ones we’ve seen and the frequency.
        l	0, 4
        o	1, 9
        v	2
        e	3, 5, 6, 11
        t	7
        c	8
        d	10

        After populating hashmap, we iterate through the hashmap and return value (idx) of the first instance of a key (character) with a value of length 1. If we can’t find it, then return -1

        """

        freq_map = defaultdict(list)  # char : list(idx)

        for i in range(len(s)):
            freq_map[s[i]].append(i)

        for char, idx_list in freq_map.items():
            if len(idx_list) == 1:
                return idx_list[0]
                
        return -1
