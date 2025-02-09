class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True

        return False