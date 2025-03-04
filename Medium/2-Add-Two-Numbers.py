 Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        carry = 0
        
        l1_node = l1
        l1_finished = False
        l1_val = 0

        l2_node = l2
        l2_finished = False
        l2_val = 0

        results_head = ListNode(val = None)
        results_node = results_head

        while True:
            if l1_finished:
                l1_val = 0
            else:
                l1_val = l1_node.val
                if l1_node.next == None:
                    l1_finished = True
                else:
                    l1_node = l1_node.next
            
            if l2_finished:
                l2_val = 0
            else:
                l2_val = l2_node.val
                if l2_node.next == None:
                    l2_finished = True
                else:
                    l2_node = l2_node.next
            
            result_val = l1_val + l2_val + carry
            if result_val > 9:
                result_val = result_val - 10
                carry = 1
            else:
                carry = 0
            
            if result_val == 0 and carry == 0 and l1_finished and l2_finished:
                break

            if results_node.val == None:
                results_node.val = result_val
                continue

            results_node.next = ListNode(val = result_val)
            results_node = results_node.next
        
        if results_head.val == None:
            results_head.val = 0
        return results_head




        
        
