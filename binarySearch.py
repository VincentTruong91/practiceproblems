#binary search
#time complexity -> O(logn) used binary +while loop
#(i.e. of binary 16 -> 8 -> 4 -> 2 -> 1 worse case)
#space complexity -> O(1) only used a few extra variables like l, r, and m
class Solution:
    def binarySearch(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)// 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else: #we have found our target
                return m
        return -1