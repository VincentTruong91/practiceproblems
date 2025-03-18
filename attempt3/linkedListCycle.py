class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    

class Solution:
    def linkedListCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()

        while curr != None:
            if curr not in set:
                seen.add(curr)
                curr = curr.next
            else:
                return False
        
        return True