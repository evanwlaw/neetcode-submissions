class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        valid counter
        """

        valid = 0
        i = 0

        while i < len(abbr):

            if abbr[i] == "0" or valid >= len(word):
                return False
            
            # handle nums
            nums = 0
            while i < len(abbr) and abbr[i].isdigit():
                nums = nums * 10 + int(abbr[i])
                i += 1
            if nums:
                valid += int(nums)
            
            else:
                if abbr[i] != word[valid]:
                    return False
                valid += 1
                i += 1
        return valid == len(word)