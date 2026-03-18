class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = self.head
        self.k = k
        self.count = 0
        

    def insertFront(self, value: int) -> bool:
        if self.count == self.k:
            return False
        if self.count == 0:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.head.prev = self.tail
            self.tail.next = self.head
            self.count += 1
            return True

        newNode = Node(value, self.head, self.tail)
        self.head.prev = newNode
        self.head = newNode
        self.head.prev = self.tail
        self.tail.next = self.head
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.k:
            return False
        if self.count == 0:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.head.prev = self.tail
            self.tail.next = self.head
            self.count += 1
            return True

        newNode = Node(value, self.head, self.tail)
        self.tail.next = newNode
        self.tail = newNode
        self.head.prev = self.tail
        self.tail.next = self.head
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
            return True

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
            return True

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.head
        self.count -= 1
        return True        

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()