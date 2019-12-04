class Node:
    def __init__(self, val: tuple = None):
        self.val: tuple = val
        self.prev: Node = None
        self.next: Node = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value: tuple):
        node = Node(value)

        if not self.front and not self.back:
            self.front = node
            self.back = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node

    def moveToFront(self, id: chr):
        id_node = self.search(id)

        temp = id_node.val
        while id_node != self.front:
            id_node.val = id_node.prev.val
            id_node.prev.val = temp
            id_node = id_node.prev

        id_node.prev = None
        self.front = id_node

    def search(self, id: chr):
        start: Node = self.front
        while start:
            if start.val[1] == id:
                return start
            start = start.next

        raise Exception("id not found")

    def print(self):
        start: Node = self.front
        print("The order is:")
        while start:
            print("({}, {})".format(start.val[0], start.val[1]))
            start = start.next


def queue_up():
    N = int(input("Enter N:"))
    print("Enter (token no, id):")

    q = Queue()

    while N:
        item: str = input()
        value: tuple = (int(item[1]), item[4])
        q.enqueue(value)
        N -= 1

    k = input("Enter k:")
    q.moveToFront(k)
    q.print()
