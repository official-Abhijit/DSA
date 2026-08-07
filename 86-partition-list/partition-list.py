class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        current = head

        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next

            current = current.next

        large.next = None
        small.next = large_dummy.next

        return small_dummy.next