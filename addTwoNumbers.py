#add two numbers from two different linked lists
#the numbers being added together are reversed for linked lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy

        carry = 0
        while (l1 != None or l2 != None or carry != 0): #or because l1 can be longer than l2, vice versa
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0

            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            curr.next = ListNode(total, None)

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            curr = curr.next

        return dummy.next