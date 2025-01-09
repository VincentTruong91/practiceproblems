#use stack and hashmap
#time complexity -> O(n) because stack + hashmap was used
#space complexity -> O(n) used a for loop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { '}': '{',   ')': '(',   ']': '[' }

        for char in s:
            if char in hashmap:
                #now check if the stack has any char and if the top of the stack is the opening
                #char of the current char
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            #else represents open characters
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
          

#########################################################
#########################################################