#Traversal DFS
#Time complexity -> O(n) visit each node once and apply same amount of work to each node
# Space complexity -> depends. O(logn) for balanced tree, O(n) for unbalanced tree. Therefore, we take O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBinary(self, root:Optional[TreeNode]) -> int:
        self.res = 0#create member variable for the instance of this class,
        #so that res is accessible inside of dfs function

        #this returns height, not the diameter.
        def dfs(curr):
            if curr == None: #reach null node
                return 0

            #otherwise, recursive case
            #height of left and right subtree
            left = dfs(curr.left)
            right =dfs(curr.right)


            #we want to maybe update the result
            #and we want to return the height of the tree from curr
            self.res = max(self.res, left + right)
            return 1 + max(left,right) #we are returning the height, not the diameter, that's why we don't return self.res, we turn max of height and add 1 for the current node we are at.


        dfs(root)
        return self.res