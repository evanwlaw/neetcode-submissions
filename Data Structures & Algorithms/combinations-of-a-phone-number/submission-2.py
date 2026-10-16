class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Input: digits = "34"
                                []
                    d           e           f
            dg  dh  di      eg  eh  ei  fg  fh  fi

        backtrack -> when our combination is len of digits -> append to output

        Time: O(N * 4^N) -> each digit, we need to explore all possibilities
        Space: O(N * 4^N) -> call stack
        """

        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if not digits:
            return []
        output = []

        def backtrack(i, combination):
            if len(combination) == len(digits):
                output.append(combination)
                return
            
            for j in range(i, len(digits)):
                # go through all letters in mapped digit
                for char in digitMap[digits[j]]:
                    backtrack(j + 1, combination + char)
                    # no need to pop bc it's a string
            return
        backtrack(0, "")
        return output