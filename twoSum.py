#Hashmap strategy
#Time Complexity -> O(n)
#Space Complexity -> O(n)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}  # val -> index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in dictionary:
                return [dictionary[diff], index]
            dictionary[num] = index

#time complexity - O(n) due to itterating through n times in list
#space complexity O(n) cost on memory due to using dictionary/map

#########################################################
#########################################################

#Brute Force
#Time Complexity -> O(n^2) because of nested for loop
#Space Complexity -> O(1) no additional data structure used in memory besides ittering through the list
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(0, len(nums), 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []