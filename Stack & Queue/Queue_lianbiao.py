class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = ListNode(None)
        self.rear = self.head
        self.count = 0

    def put_in(self, data):
        node = ListNode(data)
        self.rear.next = node
        self.rear = node
        self.count += 1

    def put_out(self):
        node = self.head.next
        self.head.next = node.next
        self.count -= 1
        return node.data

    def print_queue(self):
        if self.count == 0:
            print("-----")
            print("\n")
            print("-----")
        else:
            print("-" * self.count * 6)
            node = self.head
            for i in range(self.count):
                node = node.next
                print(str(node.data).center(5, " ") + "|", end="")
            print("\n" + "-" * self.count * 6)

x = Queue()
for i in range(100, 123):
    x.put_in(i)
x.print_queue()
x.put_out()
x.print_queue()