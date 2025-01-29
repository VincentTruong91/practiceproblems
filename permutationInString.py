#sliding window
#time complexity -> O(n)
#space complexity -> O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26

        if(len(s1) > len(s2)):
            return False

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        #sliding window
        l = 0
        #start right pointer at length of s1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #CHECKS THE R POINTER
            index = ord(s2[r]) - ord('a') #get index of our count array
            #char from r was just added to window
            s2Count[index] += 1
            #it's possible now that this windows equals to s1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1 #they were the same before s2Count[index] += 1

            #CHECKS THE L POINTER
            index = ord(s2[l]) - ord('a') #index within count array
            s2Count[index] -= 1 #character just removed from the left side of window
            #if when decrement, we just made the counts equal
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        

#i.e. s1 = abc s2 = abcde, returns true without sliding the window

