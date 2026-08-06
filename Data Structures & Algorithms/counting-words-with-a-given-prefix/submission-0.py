class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output = 0

        for w in words:
            if w[:len(pref)] == pref:
                output += 1
        return output