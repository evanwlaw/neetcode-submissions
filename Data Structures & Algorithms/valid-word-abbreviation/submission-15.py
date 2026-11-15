class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        two ptrs
        """
        i, valid = 0, 0

        while i < len(abbr):
            if abbr[i] == "0" or valid >= len(word):
                return False
            
            # build num
            num = 0
            while i < len(abbr) and abbr[i].isdigit():
                num = 10 * num + int(abbr[i])
                i += 1
            if num:
                valid += num

            else:
                if abbr[i] != word[valid]:
                    return False
                i += 1
                valid += 1
        return valid == len(word)