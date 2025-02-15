#two pass with hashmap on linked list
#time complexity -> O(n)
#space complexity -> O(n)
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyLinkedListWithRandomPointer(self, head: Optional[Node]) -> Optional[Node]:
        oldToCopy = { None: None } #for the 2nd pass, what if .next of the copy node is None?

        curr = head
        while curr != None:
            copyNode = Node(curr.val)
            oldToCopy[curr] = copyNode
            curr = curr.next


        curr = head
        while curr != None:
            copyNode = oldToCopy[curr]
            copyNode.next = oldToCopy[curr.next]
            copyNode.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]