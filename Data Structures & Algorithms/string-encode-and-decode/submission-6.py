class Solution:
    """
    5#hello4#worl

    
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # get the len of word from s[i:j]
            word_len = int(s[i:j])

            #append word
            res.append(s[j + 1 : j + 1 + word_len])

            #move ptr
            i = j + 1 + word_len
        return res
