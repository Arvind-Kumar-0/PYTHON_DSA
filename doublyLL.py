class Node:
    def __init__(self,val) -> None:
        self.last = None
        self.next = None
        self.val = val
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self,val):
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node
        node.last = self.tail
        self.tail = node
        return
    
    def view(self):
        current = self.head
        while current != None:
            print(current.val,"> ",end="")
            current = current.next
new = DoublyLinkedList()
for i in range(15):
    new.push(i)
new.view()