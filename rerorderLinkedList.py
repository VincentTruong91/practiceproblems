class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderLinkedList(self, head: Optional[ListNode]) -> None:
        #first we have to find out where to split the linked list
        #find first and second half
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        #then, we want to split the first and second list
        second = slow.next
        slow.next = None

        #then, we want to reverse the second list
        prev = None
        while second != None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #after reversing the second list,  we want to combine the first and second half together
        second = prev
        first = head

        while second != None: #because second can be less than or equal
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

    