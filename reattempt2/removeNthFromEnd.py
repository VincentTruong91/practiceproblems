class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFronEnd(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right != None:
            #itterate until n reaches 0 and when right doesn't leave the list
            right = right.next
            n -= 1

        while right != None:
            left = left.next
            right = right.next

        #we then want to remove the node from the list
        #by redirecting the pointer before the removed node to the node after
        #because the left is at dummy, left is pointer at the 
        #node before the "removed node".
        left.next = left.next.next

        return dummy.next #we return dummy.next because it's where the list starts


#if the node to remove is th head node (the first node),
#it's not possible to modify the head without losing the reference
#to the rest of the list. that's why dummy is needed 
#to keep the reference of the list
