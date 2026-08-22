class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: s = "AAABABB", k = 1
        Output: 5

        Use a window to track how long our window size is?
        iterate through A
            if we keep going, we wouldnt know the number A's we have. This is a legitimate output of size 1 but not the longest. we don't know which we need to replace, this A?
            curr window -> A : 1

        iterate through A
            if we keep going, we wouldnt know the number A's we have. This is a legitimate output of size 2 but not the longest. we don't know which we need to replace, this A?
            curr window -> A : 2        
        
        iterate through A
            if we keep going, we wouldnt know the number A's we have. This is a legitimate output of size 3 but not the longest. we don't know which we need to replace, this A?
            curr window -> A : 3
    
        iterate through B
            if we keep going, we wouldnt know the number B's we have. This is a legitimate output of size 4 if we replace the B but not the longest. but how would we know that?
            curr window -> A : 3, B : 1
        
        iterate through A
            if we keep going, we wouldnt know the number A's we have. This is a legitimate output of size 4 but not the longest. we don't know which we need to replace, this A or the B? Ideally it's the B because we'd get len 5 which is largest
            curr window -> A : 4, B : 1

        iterate through B
            if we keep going, we wouldnt know the number B's we have. This is a legitimate output of size 4 but not the longest. we don't know which we need to replace, this A or the B? Previously, we replaced one of the B's. and if we do the same, we're left with one B and "5" A's.
            curr window -> A : 4, B : 2
        
        iterate through B
            if we keep going, we wouldnt know the number B's we have. This is a legitimate output of size 4 but not the longest. we don't know which we need to replace, this A or the B? Previously, we replaced one of the B's. and if we do the same, we're left with two B and "5" A's.
            curr window -> A : 4, B : 3

        So seems to me we want to replace the least frequent char in curr window len. We can find the number of replacements in current window (k) by current window length minus max frequent char in window. Need a hashmap with letter : frequency.
        In each iteration of the input s, our hashmap contains up to k replacements needed in our current window.
        
        Once we hit the max replacements (k), then move up the left side of window.

            if len of window - max frequent char == k -> update max
            
        """

        freq = {}
        output = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            freq[char] = 1 + freq.get(char, 0)

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            output = max(output, (r - l + 1))

        return output

