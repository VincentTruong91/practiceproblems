#DFS to traverse binary tree
#time complexity -> O(n) for each node, DFS visit each node only once, which performs constant work done per node, time complexity is O(n)
#space complexity -> O(n) due to using recursion, each recursive call adds a new frame to call stack. Height of tree determines depth of call stack. Worse case = skewed tree O(n), best case balanced tree O(log n), but space always consider worse case.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #base case:
        if root == None:
            return None

        temp = root.left #saves left child before left child changes
        root.left = root.right
        root.right = temp

        #recursively call function on child nodes of parent nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

