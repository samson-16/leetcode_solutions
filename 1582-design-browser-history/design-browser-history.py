class Node:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        newnode = Node(url)
        self.cur.next = newnode
        newnode.prev = self.cur
        self.cur = newnode

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val