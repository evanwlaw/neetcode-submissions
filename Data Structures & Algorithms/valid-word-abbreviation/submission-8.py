class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        two ptrs i and valid
        """
        i = valid = 0

        while i < len(abbr):
            if abbr[i] == "0" or valid >= len(word):
                return False
            
            # num
            num = 0
            while i < len(abbr) and abbr[i].isdigit():
                num = 10 * num + int(abbr[i])
                i += 1
            if num:
                valid += num
            else:
                if word[valid] != abbr[i]:
                    return False
                i += 1
                valid += 1
                num = 0
        return len(word) == valid