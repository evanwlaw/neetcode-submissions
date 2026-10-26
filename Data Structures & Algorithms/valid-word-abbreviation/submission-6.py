class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """

        """
        wordI = 0
        abbrI = 0
        
        while abbrI < len(abbr):
            if abbr[abbrI] == "0" or wordI >= len(word):
                return False
            
            # if num, build num
            num = ""
            while abbrI < len(abbr) and abbr[abbrI].isdigit():
                num += abbr[abbrI]
                abbrI += 1
            
            if num:
                wordI += int(num)
            
            else:
                if word[wordI] != abbr[abbrI]:
                    return False
                abbrI += 1
                wordI += 1
        return wordI == len(word)
