#Solution #1 -
#create a dictionary for s and compare
#if each char in t is in s
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) != len(t):
            return False
        #add to dictionary
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        #check if t is an anagram to s
        for char in t:
            if char not in dictionary:
                return False
            else:
                dictionary[char] -= 1
        values = dictionary.values()
        for value in values: 
            if value != 0:
                return False
        return True

#Time complexity - O(n+m) length of string s and t
#Space complexity - O(1) because worst case is that we have 26 different characters (constant)

#another solution is to make 2 dictionaries (one for s and t) and check if both have the same character and the same number of that character
