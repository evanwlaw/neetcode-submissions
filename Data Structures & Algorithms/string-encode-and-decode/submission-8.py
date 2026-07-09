class Solution:
    """
    hello world -> helloworld -> hello world
    
    naive is to use a delimiter like |

    need len of each word

    5hello5world - what if number is a word and what if more than 9 char?

    use str len + delimiter 

    5#hello6#worlds
    0123456
     i
    j
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # get the len of str
            while s[i] != "#":
                i += 1
            length = int(s[j:i])

            # put str in output
            # i + 1: i + length + 1
            res.append(s[i+1 : i + length + 1])
            i = i + length + 1
        return res


