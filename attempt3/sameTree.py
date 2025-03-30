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


        if (p != None and q != None) and (p.val == q.val):
            return self.sameTree(p.left, p.right) and self.sameTree(q.left, q.right)
        

        #first condition when false means that either p or q node doesn't exist when the other one does. second condition is checking if both tree nodes p and q have the same value, and if not, return False
        return False
    

    #Itterative DFS solution: pre-order traversal
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ItterativeDFSSolution:
    def sameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        stack = [(p,q)] #use tuple to avoid confusion and reduce overhead, more efficient

        while stack: #when stack is not empty
            node1,node2 = stack.pop()

            if node1 == None and node2 == None:
                continue #reached after leaf node

            if node1 == None or node2 == None or(node1.val != node2.val):
                return False
                #this means if node1 from p doesn't exist while node2 from q exists
                # or vice versa, or if they both exist,
                #if their values don't match, return False

            
        return True