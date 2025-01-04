#Hashmap/Dictionary Solution:
#Time complexity = O(n) because we iterate over the list once and perform O(1) operations inside the loop. Hence O(1) * O(n) = O(n)
#Space complexity = O(n) because for worse case, we store all n unique numbers in the dictionary

from typing import List #import this module and use this specific class
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#optimized solution in O(n) time and 0(n) space complexity
        dictionary = {}
        for (number : nums):
            if(number not in dictionary):
                dictionary[number] = 1
            else:
                return True
        return 
        


##########################################################
##########################################################

#Hashset Solution:
#Time Complexity -> O(n)
#Space Complexity -> O(n)
from typing import List
class Solution:
    def hasDuplicate(self, List[int] nums):
        checkedAlready = set()
        for(number : nums):
            if(number in checkedAlready):
                return True
            else:
                checkedAlready.add(number)
        return False

##########################################################
##########################################################

#Brute force
#Time complexity -> O(n^2)
#Space complexity -> O(1)
from typing import List
class Solution:
    def hasDuplicate(self, List[int] nums):
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] == nums[j]:
                    return True
        return False