#Recursion DFS
#time complexity -> O(n) due to lookup at each node and applying same work on every node
#space complexity -> depends. Best case O(logn) if balanced tree, worst case O(n) if unbalanced tree. Therefore, always take worst case O(n).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True


        if (p != None and q != None) and (p.val == q.val){
            return self.sameTree(p.left, p.right) and self.sameTree(q.left, q.right)
        }
        else: #first condition when false means that either p or q node doesn't exist when the other one does. second condition is checking if both tree nodes p and q have the same value, and if not, return False
            return False
        



#Itterative DFS Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Optional

class ItterativeDFSSolution:
    def sameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack: #when stack is not empty
            nodeP, nodeQ = stack.pop()

            if nodeP == None and nodeQ == None:
                return True
            
            if nodeP == None or nodeQ == None or nodeP.val != nodeQ.val:
                #if either one exists and the other doesn't exist or both do exist but their values
                #don't match with each other
                return False
            
            stack.append((nodeP.left, nodeP.right))
            stack.append((nodeQ.left, nodeQ.right))


        return True