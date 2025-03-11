class Solution:
    def containsDuplicate(self, s:str) -> bool:
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
            else:
                return True
        
        return False
    

#time complexity -> O(n) worse case due to using a for loop to itterate over s
#space complexity -> O(n) due to using a set to store seen characters

