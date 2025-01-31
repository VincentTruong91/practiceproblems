#use set within linked list
#Time Complexity -> O(n) due to while loop
#Space complextiy -> O(n) because used set in memory

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def hasCycle(def, head:Optional[ListNode]) -> bool:
        seenNodeSet = set()
        currentNode = head

        while currentNode != None:
            if currentNode not in seenNodeSet:
                seenNodeSet.add(currentNode)
                currentNode = currentNode.next
            else:
                return True
        return False



#there's also a two pointer (slow turtoise and fast rabbit method)
#Time complexity -> O(n) due to while loop
#Space complexity -> O(1) no data structure in memory

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def hasCycle(self, head:Optional[ListNode]):
        slow, fast = head

        while fast != None and fast.next != None: #because fast goes 2 nodes each time
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False