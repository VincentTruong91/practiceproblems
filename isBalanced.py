class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursionDFSSolution:
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        def dfs(root):
            #base case
            if root == None:
                return [True, 0]
            
            #recursive case
            left, right = dfs(root.left), dfs(root.right)

            balancedHeight = abs(left[1] - right[1])
            #a balanced tree is when the left and right subtree's height has a
            #difference of no more than 1 in height.
            balanced = left == True and right == True and balancedHeight <= 1
            return [balanced, 1 + max(left[1], right[1])]


        return dfs(root)[0]
    

#time complexity -> O(n)
#space complexity -> worse case O(n)