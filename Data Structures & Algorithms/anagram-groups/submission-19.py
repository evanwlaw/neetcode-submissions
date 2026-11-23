from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hashmap -> {(word count) : [anagram1, anagram2]}
        word count = 00010020003....

        Time: O(N*M) - n is the num of words and m is the longest word in strs
        Space: O(N) - n is the number of words we need to fit into hashmap 
        """

        hashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord("a") - ord(c)] += 1
            hashMap[tuple(count)].append(word)
        
        return list(hashMap.values())
