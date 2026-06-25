class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Input: string of n length of chars (string doesnt seem constrained to just alphabetical chars)
        Output: int of the length of longest substring (needs to be contiguous and not be subsequence)

        a b c a b b c b b
                    l
                    r

        a : 0
        b : 1
        c : 2

        Idea: Use a sliding window defined by ptrs left and right. Window grows as long as we havent seen input[right]. The length of window is (right - left + 1) and finding the max window would give us the max length of a substring without repeating characters.
        
        Use set to keep track of what we've seen.
        As we iterate through input, if the char at the right ptr is in the set, then remove input[left] from the set. Need to keep moving left as long as the char at right is still in the set.
        Otherwise, if it's a new char add it to the set.
        We check if this gives us the max window length (max substring).

        Time Complexity: O(n) - We need to iterate through the entire input string. However there is a possibility we would need to iterate in the nested loop on values we already saw. So the worst case would be O(2n) which simplifies to O(n). 
        Space Complexity: O(max(n, m)) - The set would use extra space. m is the number of unique chars in the input. And worst case, every char in the input is unique, O(n). So it would depend on the input if complexity is O(m) or O(n). 

        '''
        seen = set()
        max_window = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_window = max(max_window, (right - left + 1))
        return max_window
