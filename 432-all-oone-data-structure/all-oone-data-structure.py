class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.where = {}

    def _insert_after(self, node, new_node):
        nxt = node.next

        node.next = new_node
        new_node.prev = node

        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.where:
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.where[key] = node
            return

        node = self.where[key]
        next_node = node.next

        if next_node != self.tail and next_node.count == node.count + 1:
            target = next_node
        else:
            target = Node(node.count + 1)
            self._insert_after(node, target)

        target.keys.add(key)
        self.where[key] = target

        node.keys.remove(key)

        if not node.keys:
            self._remove_node(node)

    def dec(self, key: str) -> None:
        node = self.where[key]

        if node.count == 1:
            del self.where[key]
        else:
            prev_node = node.prev

            if prev_node != self.head and prev_node.count == node.count - 1:
                target = prev_node
            else:
                target = Node(node.count - 1)
                self._insert_after(node.prev, target)

            target.keys.add(key)
            self.where[key] = target

        node.keys.remove(key)

        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))