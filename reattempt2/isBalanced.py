class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right



class RecursiveDFSSolution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #base case:
            if root == None: #if current node is a leaf node
                return [True, 0]
            
            #recursive case:
            left, right = dfs(root.left), dfs(root.right)

            #when current node has left and right child node and difference of subtree height is less than or equal to 1
            balanced = left[0] != False and right[0] != False and abs(left[1] - right[1]) <= 1

            return [balanced,1+ max(left[1], right[1])]
        
        return dfs(root)[0]
    

#time complexity -> O(n) apply equal work to all nodes from tree
#space complexity -> depends..
#O(logn) if balanced tree, where n represents height for space comp
#O(n) if unbalnaced, where n also represents height for space comp