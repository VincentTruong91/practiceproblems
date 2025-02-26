class Solution:
    def longestRepeatingCharacterReplacement(self, s:str, k:int) -> int:
        l = 0
        res = 0
        hashM = {}
        mostFreqC = 0

        for r in range(len(s)):
            hashM[s[r]] = 1 + hashM.get(s[r], 0)
            mostFreqC = max(mostFreqC, hashM[s[r]])

            #while the length of the window - most frequent character > k
            while (r - l) + 1 - mostFreqC > k:
                hashM[s[l]] -= 1
                l += 1
            res = max(res, (r - l) + 1)

        return res
    

    #time complexity -> O(n) -> characters from string s
    #space complexity -> O(m) - > m represents num of characters stored in hash
    #sliding window 2 pointer optimal solution
