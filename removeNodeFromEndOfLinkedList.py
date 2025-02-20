class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodeFromEndOfLinkedList(self, head: Optional[ListNode], n : int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #step 1: we need to find out which node to remove
        l,r = dummy, head
        N = 0

        while (N < n):
            N += 1
            r = r.next
        
        #step 2: we want to move left and right pointer to find the node that should be removed
        #this means that the node after left will be removed
        while r != None:
            l = l.next
            r = r.next

        #now we remove the target node
        l.next = l.next.next

        return dummy.next