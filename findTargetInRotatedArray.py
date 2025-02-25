class Solution:
    def findTargetInRotatedArray(self, nums:List[int], target: int) -> int:
        #returns the index of where the target is located in nums, returns -1 if not found
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
        
            #check what side of m is sorted, left or right?
            #we will use the sorted side to determine if that side contains the target
            #if not, then reduce that side. if it does, then reduce the other side

            if nums[m] >= nums[l]: #[3,4,5,6,1,2]
                #left is sorted
                #now check if left contains target
                if nums[l] >= target and nums[m] <= target:
                    #this means that left sorted does contain target
                    r = m - 1
                else:
                    l = m + 1 #this means that the right contains target
            else:
                #this means that right is sorted
                #now check if right contains the target
                if nums[m] <= target and nums[r] >= target:
                    l = m + 1
                else:
                    #this means that the left contains target
                    r = m - 1
            
        return -1


#time complexity -> O(logn)
#space complexity -> O(1)