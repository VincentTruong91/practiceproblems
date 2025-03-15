class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# e.g.
# 3 -> 4 -> 7 (743)
# 1 -> 3 -> 4 -> 1 (1431)
#
# results in:
# 4 -> 7 -> 1 -> 2
#answer: 2174, no need to worry about reversing list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        #or I can do dummy = ListNode()

        while list1 != None or list2 != None:
            carry = 0 #need a way to store the carry
            val1 = list1.val if list1 != None else 0
            val2 = list2.val if list2 != None else 0

            totalVal = val1 + val2 + carry
            carry = totalVal // 10 #e.g 7 + 4 = 11 -> 11 // 10 = 1, carry = 1
            finalValue = totalVal % 10 #e.g. 11 % 10 = 1, or 4 % 10 = 4

            ListNode(finalValue, curr)
            curr = curr.next
    
            list1 = list1.next
            list2 = list2.next

        return dummy.next


#time complexity -> O(n) due to using a while loop and going thorugh all nodes
#space complexity -> O(1) due to not using any list to store in space