class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class golfers:
    def __init__(self):
        self.head = None

    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def sortscore(self, name, score):
        current = self.head
        if current == None or score < self.head.data[1]:
            self.push([name, score])
            return
        else:
            currentdata = current.data[1]
            while current != None:
                if score >= currentdata:
                    current = current.next
                    if current == None:
                        self.append([name,score])
                        return
                    else:
                        currentdata = current.data[1]
                else:
                    self.insert(current.prev,[name,score])
                    return

    def yank(self,name):
        current = self.head
        if current.data[0] == name:
            self.head = current.next
            return
        current = self.head
        while current != None:
            if current.data[0] == name:
                current.prev.next = current.next
                return
            else:
                current = current.next
        print("404")

    def update(self,name,score):
        current = self.head
        while current != None:
            currentname = current.data[0]
            if currentname == name:
                current.data[1] = score
                if current.prev == None:
                    self.head = current.next
                    self.sortscore(name,current.data[1])
                else:
                    current.prev.next = current.next
                    self.sortscore(name, current.data[1])
                return
            current = current.next
        print("404")

    def retrieve(self,name):
        current = self.head
        while current != None:
            currentname = current.data[0]
            if name == currentname:
                print("players with same scores as", name)
                currentscore = current.data[1]
                print(current.data)
                next = current.next
                prev = current.prev
                while prev != None and prev.data[1] == currentscore:
                    print(prev.data)
                    prev = prev.prev
                while next != None and next.data[1] == currentscore:
                    print(next.data)
                    next = next.next
                return
            current = current.next
        print("404")

    def listify(self):
        thelist = []
        current = self.head
        while current != None:
            currentdata = current.data
            thelist.append(currentdata)
            current = current.next
        print(thelist)

    def revlistify(self):
        thelist = []
        current = self.head
        while current != None:
            currentdata = current.data
            thelist.append(currentdata)
            current = current.next
        thelist.reverse()
        print(thelist)

g = golfers()
g.sortscore("sus",50)
g.sortscore("amongus",73)
g.sortscore("joe",44)
g.sortscore("mama",66)
g.sortscore("big",44)
g.sortscore("chungus",44)
g.sortscore("deez",73)
g.sortscore("nuts",55)
g.listify()
g.revlistify()
g.retrieve("joe")
g.retrieve("deez")
g.yank("joe")
g.yank("mama")
g.listify()
g.update("chungus",80)
g.update("nuts",33)
g.update("sus",65)
g.listify()