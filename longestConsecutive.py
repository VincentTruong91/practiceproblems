#hashset
#time complexity -> O(n) because of for loop + while
#space complexity -> O(n) in memory because uses hashset as a data structure
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]):
        hashset = set(nums)
        
        longest = 0
        for num in hashset:
            if num-1 in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                longest = max(longest, length)

        return longest

#######################################################
#######################################################

