class Node:
    def __init__(self,v):
        self.val = v
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        i = 0
        trav = self.head
        if not trav:
            return -1
        while i<index and trav.next:
            trav = trav.next
            i+=1
        if i==index and trav:
            return trav.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        trav = self.head
        while trav.next:
            trav = trav.next
        trav.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
        trav = self.head
        while i<index-1 and trav and  trav.next:
            trav = trav.next
            i+=1
        if not trav:
            return
        tmp = trav.next
        trav.next = Node(val)
        trav.next.next = tmp
        

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        next = self.head
        while next!=None and index!=0:
            prev =next
            next = next.next
            index-=1
        if index==0 and prev != None and next != None:
            prev.next = next.next
        elif index ==0 and prev == None and next!=None:
            self.head = next.next
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)