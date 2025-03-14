class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def binarySearch(self, root: Optional[TreeNode], target:int) -> bool:
        l = 0 
        r = len(root) - 1

        while (l <= r):
            m = (r - l) // 2

            if target < m:
                r = m - 1
            elif target > m:
                l = m + 1
            else:
                return True
            
        return False
    
#time complexity -> O(n)
#space complexity -> depends O(logn) for balanced
#O(n) for unbalanced tree