class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int) # char : 1

        for c in s:
            freq[c] += 1
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1