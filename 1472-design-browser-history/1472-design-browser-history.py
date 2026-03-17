class DllNode:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = DllNode(homepage)
        self.tail = self.head
        self.curr = self.head

    def visit(self, url: str) -> None:
        newNode = DllNode(url, None, self.curr)
        self.curr.next = newNode
        self.curr = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)