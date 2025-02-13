class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next
    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr != None:
            if curr in seen:
                return True
            else:
                seen.add(curr)
                curr = curr.next
        return False