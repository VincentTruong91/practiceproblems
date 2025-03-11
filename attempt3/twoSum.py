class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #key,value = number,index

        for i in range(len(nums)):#can also use enumerate
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i
    
        return [-1, -1] #if none is found