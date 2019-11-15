class OrderedLinkedList(object):
    class _Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, lst=[]):
        self.head = OrderedLinkedList._Node(0)

    def add(self, value):
        def _add(node, value):
            # recursive.
            if node is None:
                return OrderedLinkedList._Node(val)

            if val < node.val:
                return OrderedLinkedList._Node(val, node)

            node.next = _add(node.next, val)
            return node

        self.head.next = _add(self.head.next, val)
