class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse this group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect previous part with reversed group
            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start