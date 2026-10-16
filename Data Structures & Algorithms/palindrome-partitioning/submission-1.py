class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]

                         []
                [a]     [aa]    x[aab]
            [a,a]      [aa,b]
        [a,a,b] x[a,ab]
        """
        res = []
        substrings = []
        
        def findPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i == len(s):
                res.append(substrings[:])
                return

            for j in range(i, len(s)):
                if findPalindrome(i, j):
                    substrings.append(s[i:j+1])
                    backtrack(j + 1)
                    substrings.pop()
            return
        backtrack(0)
        return res
