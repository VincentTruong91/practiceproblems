class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = 0, nums[i - 1]
            while l < r:
                sumOfThree = a + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

        return res
    

#time complexity -> O(n^2)
#space complexity -> O(1) or O(n)