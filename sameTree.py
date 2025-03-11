#Recursion DFS
#time complexity -> O(n) due to lookup at each node and applying same work on every node
#space complexity -> depends. Best case O(logn) if balanced tree, worst case O(n) if unbalanced tree. Therefore, always take worst case O(n).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True


        if (p != None and q != None) and (p.val == q.val):
            return self.sameTree(p.left, p.right) and self.sameTree(q.left, q.right)
        

        #first condition when false means that either p or q node doesn't exist when the other one does. second condition is checking if both tree nodes p and q have the same value, and if not, return False
        return False
        



#Itterative DFS Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

class ItterativeDFSSolution:
    def sameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack: #when stack is not empty
            nodeP, nodeQ = stack.pop()

            if nodeP == None and nodeQ == None:
                return True
            
            if nodeP == None or nodeQ == None or nodeP.val != nodeQ.val:
                #if either one exists and the other doesn't exist or both do exist but their values
                #don't match with each other
                return False
            
            stack.append((nodeP.left, nodeP.right))
            stack.append((nodeQ.left, nodeQ.right))


        return True
    


#Itterative BFS solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque

class ItterativeBFSSolution:
    def sameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        queueP = deque([p])
        queueQ = deque([q])

        while queueP and queueQ:
            for _ in range(len(queueP)):
                nodeP, nodeQ = queueP.popleft(), queueQ.popleft()

                if nodeP == None and nodeQ == None:
                    return True
                
                if nodeP == None or nodeQ == None or nodeP.val != nodeQ.val:
                    return False
            
                queueP.append(nodeP.left)
                queueP.append(nodeP.right)

                queueQ.append(nodeQ.left)
                queueQ.append(nodeQ.right)
            

        return True