#time complexity -> O(nlogn) + O(n^2) = O(n^2)
#space complexity -> O(1) or O(n) depending on whether or not sorting uses extra memory on libraries
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                #don't want to reuse the same value twice
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: #all three values equal to 0
                    result.append([a, nums[l], nums[r]])

                    #update pointers
                    #no need to worry about right pointer because the if from above takes care of it
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result