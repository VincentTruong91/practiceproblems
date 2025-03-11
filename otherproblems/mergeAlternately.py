class TwoPointerSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        #two pointer will be used (one for each string)
        pointerOne = 0
        pointerTwo = 0

        while pointerOne < len(word1) or pointerTwo < len(word2):
            #used an or statement becuase if either one pointer
            #has reached to the end, it still runs
            # and adds the other characters to the result
            if pointerOne < len(word1):
                result.append(word1[pointerOne])
                pointerOne += 1

            if pointerTwo < len(word2):
                result.append(word2[pointerTwo])
                pointerTwo += 1

        return "".join(result)


#time complexity -> O(n) due to itterating over word1 and 2 (this is O(length of word1 + length of word2)).
#space complexity -> O(n) where n is length of word1 and word2 that is stored in result.



class OnePointerSolution:
    def mergeAlternative(self, word1: str, word2: str) -> str:
        result = []
        word = max(len(word1), len(word2))
        #we are grabbing the longest word to take both
        #strings into account when itterating
        #and combining both strings together
        pointer = 0

        while pointer < len(word):
            if pointer < len(word1):
                result.append(word1[pointer])
            
            if pointer < len(word2):
                result.append(word2[pointer])

            pointer += 1


        return "".join(result)
    

#time complexity -> O(n)
#space complexity -> O(n)