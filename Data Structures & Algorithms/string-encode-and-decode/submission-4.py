class Solution:

    def encode(self, strs: List[str]) -> str:
        # len of str and use delimiter
        # 5#Hello5#World
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # could be like 10#characters
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            str_len = int(s[i:j])

            res.append(s[j + 1 : j + 1 + str_len])
            i = j + str_len + 1
        return res