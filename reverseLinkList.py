#Itteratively
#Time complexity -> O(n) due to using while loop
#Space complexity -> O(1) no data structure, just pointers
#Definition for a singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #step 0: assign prev pointer to null and curr pointer to first node on linked list
        prev = None
        curr = head

        #step 1: loop until curr pointer reaches to end or original linked list
        while curr:
            #step 2: save all other nodes from linked list before cutting it off
            tmp_nxt = curr.next
            #step 3: cut the curr pointer pointing to curr.next and repoint it to prev
            curr.next = prev
            #step 4: move the prev pointer to curr location
            prev = curr
            #step 5: move curr pointer to the head of all other nodes that was temp saved
            curr = tmp_nxt

        #step 6: should return prev because prev is new head in reverse link list
        return prev


# Recursively
#time complexity -> O(n)
#space complexity -> O(n)

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case:
        #if reached to the end of linked list or no nodes
        if not head:
            return None

        newHead = head #tracks new head of reversed list
        #recursive case: (reach end of linked list)
        if head.next != None: #if current node has next node
            newHead = self.reverseList(head.next) #new head will eventually reach to the end of list, which is correct

            #since head.next is the next node of head, it should reverse that link as recursion unwinds
            head.next.next = head
        head.next = None
    
        return newHead

    #i.e. 1 -> 2 -> 3 -> 4
    #steps:
    #reach end of list
    #reverse links as recursion unwinds
    #return new head of reversed list

    #self.reverselist(<1,2,3,4>)
    #head = 4
    #head = 3 (unwind), head.next.next = head, 3 <- 4
    #head = 2 (unwind), head.next.next = head, 2 <- 3
    #head = 1 (unwind), head.next.next = head, 1 <- 2
    #head.next = none

