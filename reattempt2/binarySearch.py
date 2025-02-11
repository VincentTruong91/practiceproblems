class Solution:
    def binarySearch(self, nums: List[int], int target) -> int:
        l = 0
        r = len(nums) - 1
        #assuming that nums is already sorted
        while l <= r:
            m = ((r - l) // 2) + l #or l + r / 2 but can lead to overflow

            if nums[m] < target:
                l += m + 1

            elif nums[m] > target:
                r -= m - 1

            else:
                return m
        return -1