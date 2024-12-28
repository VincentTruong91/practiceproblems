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

