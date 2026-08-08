class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        # Reverse the required part
        for _ in range(right - left):
            next_node = current.next

            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next