class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """


        turn s1 into bitmap e.g. 0101010 -> s1_count
        do the same with s2 but only up to len(s1) -> s2_count

        first check if s1_count == s2_count -> true

        for len of after s1_count to end of s2

        """
        
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len: return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(s1_len):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count: return True

        for i in range(s1_len, s2_len):
            s2_count[ord(s2[i - s1_len]) - ord('a')] -= 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            if s1_count == s2_count: return True

        return False