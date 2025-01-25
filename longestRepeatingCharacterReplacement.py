#sliding window
#time complexity -> O(m * n) #m is number of char 0-26, and n is length of string
#space complexity -> O(n) due to using hashmap in memory
class Solution:
    def longestRepeatingCharacterReplacement(self, s: str, k: int):
        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            #while the sliding window - length of most char (leftover of what char we need to replace with), is greater than k
            #remove char from map until we have enough k number of char to add into the window
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) #or is our new window the max value
        return res
