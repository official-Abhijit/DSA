class Solution:
    def swapPairs(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            # Swap the two nodes
            first.next = second.next
            second.next = first
            previous.next = second

            # Move to the node before the next pair
            previous = first

        return dummy.next