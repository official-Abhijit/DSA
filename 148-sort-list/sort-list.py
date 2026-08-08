class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find length
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        dummy = ListNode(0, head)
        size = 1

        while size < length:
            prev = dummy
            current = dummy.next

            while current:
                left = current
                right = self.split(left, size)
                current = self.split(right, size)

                merged_head, merged_tail = self.merge(left, right)

                prev.next = merged_head
                prev = merged_tail

            size *= 2

        return dummy.next

    def split(self, head, size):
        if not head:
            return None

        for _ in range(size - 1):
            if not head.next:
                break
            head = head.next

        next_part = head.next
        head.next = None

        return next_part

    def merge(self, first, second):
        dummy = ListNode(0)
        tail = dummy

        while first and second:
            if first.val <= second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            tail = tail.next

        tail.next = first if first else second

        while tail.next:
            tail = tail.next

        return dummy.next, tail