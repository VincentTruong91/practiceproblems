class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int, int]:
        hashmap = {}

        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup not in hashset:
                hashset[nums[i]] = i
            else:
                return [hashmap[lookup], i]

        return [,]