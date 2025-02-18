class Solution:
    def twoSumPartTwo(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if (numbers[left] + numbers[right]) < target:
                left += 1
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            else:
                return [left, right]
            
        return []
    

#two pointers solution:
#time complexity -> O(n) due to using while loop itteration
#space complexity -> O(1) didn't use set or hashmap (which would've been O(n) if used.)

