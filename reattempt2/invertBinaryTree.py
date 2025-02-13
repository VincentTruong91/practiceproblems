#DFS
#time comp O(n) due to going through all nodes in tree
#space comp O(n) worse case through unbalanced tree and apply equal work to all nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optonal[TreeNode]:
        #recursion

        #base case
        if root == None:
            return 
        
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursive
        #this means that the function recursively calls itself
        #on the lefrt and right subtrees (which are swapped)
        #It will keep inverting the subtrees of the current node until
        #it reaches to all leaf nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

