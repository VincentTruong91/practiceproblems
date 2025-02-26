class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            seen.add(s[r])
            res = max(res, len(seen))

        return res
    
#time complexity -> O(n) used for loop
#space complexity -> O(n) due to using set
#method used sliding window via 2 pointers

