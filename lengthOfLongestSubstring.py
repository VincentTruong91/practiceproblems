#sliding window/two pointer
#time complexity -> O(n) total number of char in the string
#space complexity O(m) total number of unique char in string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        #r in this case will represent the right pointer
        for r in range(len(s)):
            #if r is a duplicate from discovered
            while s[r] in charSet:
                #move the left pointer until right pointer char is no longer a dup
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res
