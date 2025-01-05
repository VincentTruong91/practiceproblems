#Hashmap/Dictionary solution
#Time complexity -> O(n) uses forloop
#Space complextiy -> O(n) because uses hashmaps
class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        dictionaryS = {}
        dictionaryT = {}
        for i in range(len(s)):
            dictionaryS[s[i]] = 1 + dictionaryS.get(s[i], 0)
            dictionaryT[t[i]] = 1 + dictionaryT.get(t[i], 0)
        
        return dictionaryS == dictionaryT

##################################################################
##################################################################

#Sorted function
#Time complexity -> O(nlogn) becasue we are using the sorted algoritm
#Space complexity -> O(1) because we aren't using any data structure
class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)