#linked list itteration pointer
#time complexity -> O(l1+l2) n is for list1 and m is for list2 = O(n)
#space complexity -> O(1) no data structure used in memory
#Definition of a singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoSortedLinkedList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = node = ListNode()

        while list1 != None and list2 != None:
            if list1 < list2:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        if list1 != None:
            node.next = list1
        elif list2 != None:
            node.next = list2

        head = dummy.next
        return head