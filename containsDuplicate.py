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


#Time complexity = O(n) because we iterate over the list once and perform O(1) operations inside the loop. Hence O(1) * O(n) = O(n)

#Space complexity = O(n) because for worse case, we store all n unique numbers in the dictionary