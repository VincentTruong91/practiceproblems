class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Solution DFS
class RecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    


#ItterativeSolution DFS (using stack)
class ItterativeSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        #everytime we go through a level, we pop the node
        while stack: 
            node, depth = stack.pop() #[node, depth] from stack

            # don't add to stack if node is null
            if node != None:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res


#BFS (breadth first search, using deque (double ended queue))
from collections import deque
class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root != None:
            return 0
        
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level