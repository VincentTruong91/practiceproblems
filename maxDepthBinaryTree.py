#Recursive DFS
#Time Complexity -> O(n) DFS visits each node once and constant work is done at each node
#Space complexity -> O(n) determined by the maximun depth of the call stack. best case = O(logn) for a balanced tree, worst case = O(n) for an unbalanced tree. space always takes worse case. Therefore, O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root: Optional[TreeNode]):
        #Recursive DFS
        #base case
        if root == None: #empty tree
            return 0

        #else there is a tree
        #recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
