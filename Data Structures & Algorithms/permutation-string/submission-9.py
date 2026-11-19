class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord('a') - ord(s1[i])] += 1
            s2Count[ord('a') - ord(s2[i])] += 1
        
        if s1Count == s2Count:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2Count[ord('a') - ord(s2[r])] += 1
            while r - l + 1 > len(s1):
                s2Count[ord('a') - ord(s2[l])] -= 1
                l += 1
            if s1Count == s2Count:
                return True
        return False