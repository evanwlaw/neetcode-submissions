class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(i, currStr):
            if len(digits) == len(currStr):
                res.append(currStr)
                return 
            for c in combinations[digits[i]]:
                dfs(i + 1, currStr + c)
        if digits:
            dfs(0, "")
        return res