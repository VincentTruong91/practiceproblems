#binary search
#time complexity -> O(log n) using binary search
#space complexity -> O(1) only using variables (res, l , r)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        # i.e. [1], we still want to check 1 when both pointers are pointing at 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            #check if left is sorted
            if nums[m] >= nums[l]:
                #check if target not in left sorted
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: #it's in sorted left side
                    r = m - 1
            else: #right is sorted
                #check if target not in right sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1