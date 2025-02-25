class Solution:
    def findMinInRotatedArray(self, nums: List[int]) -> int:
        
        res = nums[0]

        l = 0, r = len(nums) - 1
        while l <= r:

            if nums[l] < nums[r]:
                #this means that the current state of the array is sorted
                #through any itteration
                res = min(res, nums[l])
                break

            
            #make it to this means that it's currently unsorted
            m = (r + l) // 2
            #[3,4,5,6,1,2] --> [6,1,2]
            # l   m     r       l m r
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                #then we trunkate the left half of the rotated array
                l = m + 1
            else:
                r = m - 1

        return res

            
