#recursion dfs
#time complexity -> O(n) apply the same amount of work to all nodes due to recurion and visit every node
#space complexity -> depends O(h), if balanced tree O(logn) best case, if unbalanced worst case O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, tree:Optional[TreeNode]):
        def dfs(root):
            if root == None: #if our current node is a leaf node or if tree has no elements
                return [True, 0] #balanced.

            left, right = dfs(root.left), dfs(root.right)

            balanced = False
            if left[0] == True and right[0] == True and ( abs(left[1] - right[1] <= 1) ):
                balanced = True
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]