#binary search
#time complexity -> O(n + log m) due to using for loop in binary search
#space complexity -> O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #grab the highest pile of bananas from the list of bananas
        res = r #rate that koko eats (set to highest, but we want to find the smallest eat rate of bananas that koko can eat within the alloted hour time (h))

        while l <= r:
            k = (l + r) // 2 #k is how many koko eats per hour
            hours = 0 #how much time koko spends eating
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h: #if hours from koko's given eat rate is less than the rate needed to eat
                res = max(res, k) #either new rate of koko eating vs. saved max rate that koko eats, is faster
                r = k - 1
            else:
                l = k + 1 #koko couldn't finish on time

        return res