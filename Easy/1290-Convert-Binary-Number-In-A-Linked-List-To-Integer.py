class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value: int = 0
        while True:
            value += head.val
            if head.next == None:
                break
            head = head.next
            value = value * 2
        return value
