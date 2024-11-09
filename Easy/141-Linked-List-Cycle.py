# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        if head == None:
            return False
        
        current_node = head
        seen[head] = True

        if head.next == None:
            return False

        current_node = head.next
        while current_node.next != None:
            if current_node in seen:
                return True
            seen[current_node] = True
            current_node = current_node.next
        return False
