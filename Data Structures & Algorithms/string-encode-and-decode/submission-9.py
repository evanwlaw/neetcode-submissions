class Solution:
    """
    Hello World -> encoded string -> decode to Hello World

    cant just use ints for length bc strs can contain it too

    5#Hello6#Worlds

    decode:
    1. build int while c not #
    2. append s[start:int+start] to output
    3. return output
    """
    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        # while i < len(s):
        #     sLen = 0
        #     while s[i] != "#":
        #         sLen = sLen * 10 + int(s[i])
        #         i += 1
        #     start = i
        #     output.append(s[start:sLen+1])
        #     i = i + sLen + 1
        # return output

        while i < len(s):
            sLen = 0
            while s[i] != "#":
                sLen = sLen * 10 + int(s[i])
                i += 1
            output.append(s[i+1:sLen + i + 1])
            i = i + sLen + 1
        return output