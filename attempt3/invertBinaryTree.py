class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFSRecursiveSolution:
    def invertBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root