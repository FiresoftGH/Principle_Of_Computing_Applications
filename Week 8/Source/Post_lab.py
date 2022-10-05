import names
import random
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, previous_node, new_data):
        if previous_node is None:
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        new_node.prev = previous_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def sortprintl(self):
        current = self.head
        while current is not None and current.next is not None:
            current_data = current.data
            next_data = current.next.data
            if current.data[1] > current.next.data[1]:
                current.data = next_data
                current.next.data = current_data
            current = current.next
                

    def sortprintg(self):
        pass

def playerScore():
    return [names.get_last_name(), random.randint(0, 50)]

double = doubly_linked_list()
for x in range(10):
    val = playerScore()
    double.push(playerScore())

double.sortprintl()
double.listprint(double.head)

# reverse, retrieve, 