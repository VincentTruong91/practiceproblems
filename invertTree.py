#DFS to traverse binary tree
#forgot to mention but this is preorder
#because root, left, then right
#time complexity -> O(n) for each node, DFS visit each node only once, which performs constant work done per node, time complexity is O(n)
#space complexity -> O(n) due to using recursion, each recursive call adds a new frame to call stack. Height of tree determines depth of call stack. Worse case = skewed tree O(n), best case balanced tree O(log n), but space always consider worse case.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveDFSSolution:
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


#uses stack for dfs itteration
#this also uses pre-order traversal
#nodes are processed in pre-order fashion
#for example:
#    1
#   2 3
#  4   5
#
# 1 -> 2 -> 4 -> 3 -> 5
#time complexity -> O(n) due to itterating through all nodes in tree via while loop
#space complexity -> O(n) due to using stack to apply equal work to all nodes in tree
class ItterativeDFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        stack = [root]

        while stack != None:
            node = stack.pop()

            node.left, node.right = node.right, node.left
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

            
        return root
    


#this solution 
#goes throught each node from the previous level
#and adds new children (if there are any) from the previous level
#for this current node
#Time complexity -> O(n) due to using a while loop to go through each node
#space complexity -> O(n) due to applying equal work to all nodes for all nodes and
# using a queue to store nodes
from collections import deque
class ItterativeBFSSolution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        queue = deque([root]) #a list is passed, which is itteratble
        #if i did queue = deque(root), it's not itterable, since it's a single node, error

        while queue != None:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        
        return root