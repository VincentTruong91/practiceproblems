class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            encodedStr += str(len(string)) + "#" + string
        return encodedStr


    def decode(self, s: str) -> List[str]:
        decodeList, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lengthOfString = int(s[i:j])
            i = j + 1 #goes to front of string
            j = i + lengthOfString #next number
            decodeList.append(s[i:j]) #add string to decode list
            i = j

        return decodeList

#time complexity - O(n) where n is the total number of characters given to us in the list of words
#space complexity - O(1) because it doesn't use any extra space since we didn't use an array to store the length of each word,
#rather, we embedded the length of the word with the '#' delimeter to determine what characters of the encoded
#sentence should be broken up to different words