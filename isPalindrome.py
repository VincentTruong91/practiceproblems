#uses string
#Time Complexity -> O(n) for loop
#space complexity -> O(n) reverse string and uses extra string ""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" #removes all alphanumeric char (use extra memory)
        
        for char in s:
            if char.isalnum(): #if alphanumerical
                newStr += char.lower()

        return newStr == s[::-1] #reverse s string uses extra memory


##############################
##############################

#two pointer
#time complexity -> O(n) due to using while loop (nested while loop is still O(n))
#space complexity -> O(1) not storing any extra memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))