class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def to_list(self):
        l = []
        if self.head is None:
            return l
        node = self.head
        while node:
            l.append(node)
            node = node.next_node
        return l

    def __str__(self):
        ll_str = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_str += f"{str(node.data)} ->"
            node = node.next_node
        ll_str += " None"
        return ll_str


if __name__ == '__main__':
    ll = LinkedList()
    [ll.insert_head(f"node {x}") for x in range(10)]
    [ll.insert_tail(f"node {x}") for x in range(10, 20)]
    print(ll)
