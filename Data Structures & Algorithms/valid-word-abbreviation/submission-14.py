class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = valid = 0

        while i < len(abbr):
            if abbr[i] == "0" or valid >= len(word):
                return False
            
            # get num
            num = 0
            
            while i < len(abbr) and abbr[i].isdigit():
                num = 10 * num + int(abbr[i])
                i += 1
            
            if num: # if it's num >0 aka we get a num/not char
                valid += num
            
            else: # else it's a char
                if abbr[i] != word[valid]:
                    return False
                i += 1
                valid += 1                

        return valid == len(word)