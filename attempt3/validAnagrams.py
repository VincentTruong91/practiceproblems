class Solution:
    def validAnagrams(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        #check if the length of both s and t are the same
        #if not, then it's impossible to have s and t as 
        #valid anagrams

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            #we can just itterate through one given string because
            #both of them are the same length
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #if they are identical, they are valid anagrams (true), otherwise false.
        return countS == countT
    
#time complexity -> O(n) due to using a for loop to itterate through string
#space complexity -> O(n) by using a hashmap to store characters

