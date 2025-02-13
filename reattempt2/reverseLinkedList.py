class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None #points to NULL/None
            curr = head #points to head
            
            while(curr != None): #while curr hasn't reached to the end of linked list
                 next_node = curr.next #store next node
                 curr.next = prev #reverse current node's pointer
                 prev = curr #prev pointer to curr node
                 curr = next_node #curr pointer to next node

            return prev #where prev points is going to be the new head
                 