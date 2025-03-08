class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursionDFSSolution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case: can be applied either when search reaches after leaf node.
        if p == None and q == None:
            return True
        
        #recursive case
        #checks if the same node exits from both trees and if their values are same if both exist.
        if p != None and q != None and (p.val == q.val):
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        return False
    

#time complexity -> O(n) due to going through all nodes and apply equal work to all nodes
#space complexity -> O(logn) if balanced tree, O(n) if unbalanced tree


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
    
#time complexity -> O(n) applied same work to all nodes in trees p and q
#space complexity -> depends, O(logn) for balanced tree
#but O(n) for unbalanced tree