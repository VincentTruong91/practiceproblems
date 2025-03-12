class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while head != None:
            next = curr.next #create next pointer
            curr.next = prev #curr node now points to prev node

            prev = curr #prev pointer at curr
            curr = next #curr pointer at next

        return prev #when head is out of linked list, prev is new head
    

#time complexity -> O(n) use while loop
#space complexity -> O(1) no data structure storage used