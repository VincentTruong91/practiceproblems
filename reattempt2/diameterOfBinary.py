class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveDFS:
    def diameterOfTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = 0 #global variable

        #give us height instead of diameter
        def dfs(curr):
            #base case
            if curr == None:
                return 0
            
            #recursive case (reach until leaf node)
            left = dfs(curr.left)
            right = self.dfs(curr.right)

            res = max(res, left + right)

            return 1 + max(left, right)


        dfs(root)
        return self.res
    

#time complexity -> O(n)
#space complexity ->O(logn) best case if balanced tree
#O(n) worst case unbalanced tree