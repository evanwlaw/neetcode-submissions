class Solution:
    """
    input -> encode into 1 str -> decode -> output into list of words
    delimiter like # to sep words. but what if # is in the str?

    helloworld is

    10#helloworld2#is

    to get len -> while c not # -> s[i : to #] is len

    iterate len times to put into word
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
        
            while s[j] != '#':
                j += 1

            s_len = int(s[i:j])

            res.append(s[j + 1 : j + s_len+ 1])
            i = j + s_len + 1
        return res
            
            