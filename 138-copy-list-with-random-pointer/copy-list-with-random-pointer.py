class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copies = {}

        current = head

        while current:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copies[current].next = copies.get(current.next)
            copies[current].random = copies.get(current.random)
            current = current.next

        return copies[head]