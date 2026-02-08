class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getNodeAt(self, index):
        if index < 0 or index >= self.size:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def addAt(self, index, value):
        if index < 0 or index > self.size:
            return

        node = Node(value)

        if index == 0:
            node.next = self.head
            self.head = node
            if self.size == 0:
                self.tail = node
        else:
            prev = self.getNodeAt(index - 1)
            node.next = prev.next
            prev.next = node
            if node.next is None:
                self.tail = node

        self.size += 1

    def addAtMany(self, index, values):
        if index < 0 or index > self.size or not values:
            return

        first = Node(values[0])
        cur = first
        for v in values[1:]:
            cur.next = Node(v)
            cur = cur.next
        last = cur
        count = len(values)

        if index == 0:
            last.next = self.head
            self.head = first
            if self.size == 0:
                self.tail = last
        else:
            prev = self.getNodeAt(index - 1)
            last.next = prev.next
            prev.next = first
            if last.next is None:
                self.tail = last

        self.size += count

    def deleteAt(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            prev = self.getNodeAt(index - 1)
            prev.next = prev.next.next
            if prev.next is None:
                self.tail = prev

        self.size -= 1

    def replaceAt(self, index, value):
        node = self.getNodeAt(index)
        if node:
            node.value = value

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    linked = LinkedList()

    nums = list(map(int, input().split()))
    linked.addAtMany(0, nums)

    for _ in range(M):
        cmd = input().split()

        if cmd[0] == 'I':
            x = int(cmd[1])
            y = int(cmd[2])
            linked.addAt(x, y)

        elif cmd[0] == 'D':
            x = int(cmd[1])
            linked.deleteAt(x)

        elif cmd[0] == 'C':
            x = int(cmd[1])
            y = int(cmd[2])
            linked.replaceAt(x, y)

    node = linked.getNodeAt(L)
    result = node.value if node else -1
    print(f"#{tc} {result}")
