class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {} #we can use .values(), .keys(), and .items()
        for number in nums: #O(n)
            #add to the value of the key without worrying about
            #if the key does or doesn't exist in the dictionary
            dictionary[number] = 1 + dictionary.get(number, 0) #O(1)
        
        #setting up bucketsort
        freq = [[] for i in range(len(nums) + 1)] #0..(n-1)+1
        for num, count in dictionary.items(): #O(n)
            freq[count].append(num) #O(1) bucket sorting element placement depends on how many elements there are in the given array

        #highest frequency of numbers is added to the result first
        result = []
        for i in range(len(freq) - 1, 0, -1): #O(k) ~= O(n)
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            

        # time complexity O(n)
        # space complexity O(n) - dictionary, frequency list, and result list takes
        # up O(n) memory