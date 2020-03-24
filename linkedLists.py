# singly-linked list

class Node:
    def __init__(self, value):
        self.item = value
        self.ref = None

class singlyLinkedList:
    def __init__(self):
        self.start_node = None
        
    def traverseSLL(self):
        if self.start_node is None:
            print("Empty")
            return 0
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=" ")
                n = n.ref
    def insertAtStart(self, value):
        new_node = Node(value)
        new_node.ref = self.start_node
        self.start_node = new_node

linkedList = singlyLinkedList()
for i in range(1,100):
    linkedList.insertAtStart(i)
linkedList.traverseSLL()


# linkedList.
# LL = Node(1)
# LL = Node(2)
# LL = Node(3)
# LL = Node(4)
# LL = Node(5)

# list = singlyLinkedList()



        
