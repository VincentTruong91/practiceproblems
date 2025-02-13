#slow,fast pointer to split into 2
#time complexity -> O(n) due to going through linked list (length of n)
#space complexity -> O(1) due to not using any arr to store values. 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def reorderLinkedList(self, head: Optional[ListNode]) -> None:
        #First, figure out where middle is at
        slow = head
        fast = head.next

        #because fast goes twice as fast, we check fast and fast.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        #now we reverse the second half
        prev = None
        while second != None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        #now reorder the list with both first and second half
        second = prev #prev is the new head of second list
        first = head
        while second != None: #the second half can either be equal or shorter in length compared to first half
            #because the chain will be broken when setting new .next to the current nodes from 
            #first and second half, we need to store the node that the current one will break from
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

