#DFS
#time comp O(n) due to going through all nodes in tree
#space comp O(n) worse case through unbalanced tree and apply equal work to all nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSRecursiveSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optonal[TreeNode]:
        #recursion

        #base case
        if root == None:
            return 
        
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursive
        #this means that the function recursively calls itself
        #on the lefrt and right subtrees (which are swapped)
        #It will keep inverting the subtrees of the current node until
        #it reaches to all leaf nodes
        self.invertTree(root.left)
        self.invertTree(root.right)


from collections import deque

class BFSSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = deque([root])

        while queue != None:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left != None:
                deque.append(node.left)

            if node.right != None:
                deque.append(node.right)
        return root
    
#time complexity -> O(n)
#space complexity -> O(n)



#Itterative DFS Solution
class DFSItterativeSolution:
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
    
#time complexity -> O(n) due to using while loop and apply same work to all nodes in tree
#space complexity -> O(n) due to using stack to store all nodes from tree