class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = []
        self.now = homepage
        self.next = []

    def visit(self, url: str) -> None:
        self.next = []
        self.prev.append(self.now)
        self.now = url

    def back(self, steps: int) -> str:
        while steps and self.prev:
            self.next.append(self.now)
            self.now = self.prev.pop()
            steps-=1
        return self.now

    def forward(self, steps: int) -> str:
        while steps and self.next:
            self.prev.append(self.now)
            self.now = self.next.pop()
            steps-=1
        return self.now


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)