#Recursive DFS
#Time Complexity -> O(n) DFS visits each node once and constant work is done at each node
#Space complexity -> O(n) determined by the maximun depth of the call stack. best case = O(logn) for a balanced tree, worst case = O(n) for an unbalanced tree. space always takes worse case. Therefore, O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Recursive DFS
        #base case
        if root == None: #empty tree
            return 0

        #else there is a tree
        #recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#########################################################
#########################################################
#BFS (Breadth First Search)
# Time Complexity -> O(n)
# Space Complexity -> O(n)

class TreeNode:
    def __init__(self, val=0,left=None,right=None) -> int:
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root=Optional[TreeNode]):
        q = deque()
        level = 0
        
        if root != None:
            q.append(root)

        while q != None:
            for i in range(len(q)): #go through all children in the same level
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            level += 1

        return level


####################################################
####################################################
#Itterative DFS (depth first search without recursion), we use pre-order traversal (root, left, right)
#
#

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root:Optional[TreeNode]):
        stack = []
        res = 0
        if root != None:
            stack.append([root, 1]) #node and level

        while stack != None:
            #we will use pre-order traversal (root, left ,right)
            node, depth = stack.pop()

            if node != None:
                res = max(res, depth)
                stack.append([node.left, depth + 1]) #if node is null it will ignore this line
                stack.append([node.left, depth + 1]) #if node is null it will also ignore this line

        return res