class Solution:
    """
    hello world -> helloworld -> hello world
    
    naive is to use a delimiter like |

    need len of each word

    5hello5world - what if number is a word and what if more than 9 char?

    use str len + delimiter 

    5#hello6#worlds

    """

    def encode(self, strs: List[str]) -> str:
        """
        str(len(s)) + '#' + s
        """
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        """
        step 1: get len of string
        step 2: append the string
        step 3: update ptr
        """
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != '#': # move j to end of word
                j += 1
            
            # len is i:j
            word_len = int(s[i:j])

            # word starts at s[j + 1]
            # word ends at s[j + 1 + word_len]

            # append str to res
            res.append(s[j+1 : j + 1 + word_len])

            i = j + 1 + word_len
        
        return res
            
            


        
