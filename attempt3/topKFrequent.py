from typing import List

class Solution:
    def topKFrequentK(self, nums: List[int], k:int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #1, add numbers from nums array into count dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #2, add numbers from count dictionary into bucketsort
        for number, cnt in count.items():
            freq[cnt].append(number)

        #step 3, decrement from the freq bucketsort
        #and add it to res array to have it returned.
        res = []
        for i in range(len(freq) - 1, 0, - 1):
            for number in freq[i]: #if there are multiple
                #numbers for a single count
                #i.e. [[3][2][1,4]] (one 3, two 2's, three 1's and three 4's) when k = 2
                res.append(number)
                if len(res) == k:
                    return res
