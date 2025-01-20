#binary search
#approach: we are going to reduce down the state of the array from the left and right sides of the array, and taking the current state of the array when the current state of the array is sorted (while having one of the element(s) as the min value in that current state)
#time complexity -> O(log n) due to using binary search (Restriction = can't use O(n))
#space complexity ->O(1) in memory due to not using any arr as storage

class Solution:
    def findMin(self, nums: List[int]):
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            #check whether or not our current reduced/non-reduced arr is sorted (while containing min value)
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            #since current state of array isn't sorted, reduce arr
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                #this means everything from left can be removed since it's rotated
                l = m + 1
            else:
                r = m - 1

        return res