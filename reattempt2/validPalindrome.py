class Solution:
    def isAlphaNum(self, c: char) -> bool:
        return (ord('a') <= ord(c) <= ord('z') ||
        ord('A') <= ord(c) <= ord('Z') ||
        ord('1') <= ord(c) <= ord('9'))
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True