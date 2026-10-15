class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        backtrack

        """

        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []

        def backtrack(i, combination):
            if len(combination) == len(digits):
                res.append(combination)
                return
            for d in digitMap[digits[i]]:
                backtrack(i + 1, combination + d)
            return
        if digits:
            backtrack(0, "")
        return res