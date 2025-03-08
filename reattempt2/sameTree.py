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