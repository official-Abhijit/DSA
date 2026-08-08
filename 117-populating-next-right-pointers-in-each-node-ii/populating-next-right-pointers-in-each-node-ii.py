class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        current = root

        while current:
            dummy = Node(0)
            tail = dummy

            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            current = dummy.next

        return root