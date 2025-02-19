class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #unsorted, has to sort O(nlogn)
        for i, number in enumerate(nums):
            if i > 0 and number == nums[i - 1]:
                #checking if this number is the same as previous number
                continue

            l, r = i + 1, len(nums) -1
            while l < r:
                sum = number + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([number, nums[l], nums[r]])
        
        return res
    

#two pointers within the ith pointer
#time complexity -> O(n^2) due to using a loop within a loop (O(nlogn) + O(n^2))
#space complexity -> space complexity O(1) or O(n)