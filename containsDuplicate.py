class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimized solution in O(n) time and 0(n) space complexity
        dictionary = {}
        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                return True
        return False