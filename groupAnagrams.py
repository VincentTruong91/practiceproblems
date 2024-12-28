class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {} #key:value -> {charCount}:{[list of Anagrams]}
        for string in strs:
            count = [0] * 26 #this keeps count on how many char there are from a thru z

            for char in string:
                count[ord(char) - ord("a")] += 1 #determines what char count should be incremented via ascii difference
                # for example if c is 76 and a is 74, c-a = 76-74 = 2
            key = tuple(count) #key is immutable, cant be changed

            if key in dictionary: #charCount sequence
                dictionary[key].append(string) #append it to the value of key in it's inner array
            else:
                dictionary[key] = [string] #create a key and a new array as its value

        return list(dictionary.values())


#time complexity - O(m*n) because it's going through the number of strings (m) and length of each string (n)

#space complexity = O(n) because it's using a dictionary which takes up a bit of memory