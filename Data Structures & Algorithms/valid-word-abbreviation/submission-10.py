class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        two ptrs

        no leading 0s
        valid < len(word)
        """
        i, valid = 0, 0

        while i < len(abbr):
            if abbr[i] == "0" or valid >= len(word):
                return False
            # get nums
            num = 0
            while i < len(abbr) and abbr[i].isdigit():
                num = 10 * num + int(abbr[i])
                i += 1
            
            if num:
                valid += num
            else:
                # no num, check if same char
                if abbr[i] != word[valid]:
                    return False
                i += 1
                valid +=1
        return valid == len(word) 
