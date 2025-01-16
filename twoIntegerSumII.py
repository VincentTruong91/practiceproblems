#two pointers
#time complexity -> O(n)
#space complexity -> O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while(l < r):
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: #value of two pointers is less than target
                l += 1

        return []


#####################################
#####################################
#hashmap
#time compelxity -> O(n)
#space complextiy -> O(n) due to using defaultdict (hashmap) in memory
class Solution:
    def twoSum(self, numbers: List[int], target: int):
        hashmap = defaultdict(int) #dictionary
        for i in range(len(numbers)):
            temp = target - i
            if hashmap[temp]:
                return [hashmap[temp], i + 1]
            hashmap[numbers[i]] = i + 1
        return [] 