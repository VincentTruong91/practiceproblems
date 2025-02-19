class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += len(string) + "#" + string
        return res

    def decode(self, string: str) -> List[str]:
        res, i = [], 0

        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
        return res
    
#basic array usage
#time complexity -> O(n) due to using for loop and while loop
#space complexity -> O(1)