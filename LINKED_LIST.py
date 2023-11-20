array =[913, 578, 245, 754, 321, 987, 502, 689, 123, 876,
        450, 265, 831, 164, 729, 593, 316, 871, 104, 618,
        937, 782, 349, 516, 190, 847, 682, 415, 578, 236,
        691, 327, 864, 509, 147, 734, 602, 879, 394, 128,
        863, 578, 241, 756, 312, 988, 508, 684, 120, 879,
        444, 269, 834, 172, 725, 589, 321, 875, 108, 612,
        943, 788, 356, 523, 196, 857, 692, 425, 588, 230,
        701, 333, 868, 524, 161, 749, 615, 892, 387, 142,
        881, 556, 223, 742, 308, 974, 489, 657, 279, 810,
        173, 926, 671, 343, 790, 258, 925, 603, 216, 671]
class Node:
    def __init__(self,val) -> None:
        self.last = None
        self.next = None
        self.val = val
class DoublyLinkedList(list):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,val):
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node
        node.last = self.tail
        self.tail = node
        self.length += 1
        return
    
    def view(self):
        current = self.head
        while current != None:
            print(" > ",current.val,end="")
            current = current.next
    def sort(self):
        sorter = []
        current = self.head
        while current != None:
            sorter.append(current.val)
            current = current.next
        
        area = len(sorter)
        
        while area > 0:
            for i in range(1,area):
                if sorter[i-1] > sorter[i]:
                    sorter[i-1] , sorter[i] = sorter[i] , sorter[i-1]
            area -= 1
        current = self.head
        index = 0
        while current != None:
            current.val = sorter[index]
            current = current.next
            index += 1
    def __len__(self) -> int:
        return self.length      
            
            
new = DoublyLinkedList()
for i in array:
    new.append(i)
new.sort()
new.view()
len(new)