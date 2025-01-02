class Solution:
    def productExceptSelf(self, nums : List[int]) -> List[int]:
        ret = [1] * len(nums)
        prefix = 1
        for i in range(0, len(nums), 1):
            ret[i] = prefix
            prefix *= ret[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= prefix
            prefix * ret[i]
        
        return ret


#O(n) time complexity b/c for loops are being used
#O(1) space complexity memory (maybe?) but also can be O(n) because additional array (ret) space was used.