class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello6#Worlds
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            # 1. get the len of string e.g. 5
            strLen = 0
            while i <= len(s) and s[i].isdigit():
                strLen = strLen * 10 + int(s[i])
                i += 1
            # 2. increment to #
            i += 1
            # 3. append to output s[i : i + strLen + 1]
            output.append(s[i : i + strLen])
            # 4. update ptrs to i = i + strLen + 1
            i += strLen
        return output