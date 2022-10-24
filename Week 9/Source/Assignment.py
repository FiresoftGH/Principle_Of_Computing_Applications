from this import d
from numpy import char


with open("firesoft.txt") as document:
    lines = document.readlines()
    contents = "".join(lines)
    username_construct = []
    password_construct = []
    for lines in contents:
        for character in lines.split():
            if character.isdigit():
                password_construct.append(int(character))

            if character.isalpha():
                username_construct.append(str(character))

    for k in range(300):
        a = tuple([username_construct[k], password_construct[k]])
        print(a)

class BST:
    def __init__(self, new_node):
        self.new_node = new_node
        self.left = None
        self.right = None

    def insert(self, new_node):
        if new_node[1] == self.new_node[1]:
            return "Error"
        
        if new_node[1] < self.new_node[1]:
            if self.left:
                self.left.insert(new_node)

            else:
                self.left = BST(new_node)

        else:
            if self.right:
                self.right.insert(new_node)

            else:
                self.right = BST(new_node)

    def find(self, new_node):
        if new_node[1] < self.new_node[1]:
            if self.left == None:
                print("The user ", str(new_node[0]), "does not exist")

            else:
                print(self.left.find(new_node[1]))
            
        elif new_node[1] > self.new_node[1]:
            if self.right == None:
                print("The user ", str(new_node[0]), "does not exist")

            else:
                print(self.left.find(new_node[1]))

        else:
            print(str(self.new_node[0]) + " is a valid user")

    def delete(self, root, key):
        if not root:
            return root

        if root.new_node > key:
            root.left = self.delete(root.left, key)

        elif root.new_node < key:
            root.right = self.delete(root.right, key)

        else:
            if not root.right:
                return root.left

            elif not root.left:
                return root.right

            else:
                operator = root.right
                min_val = operator.new_node
                while operator.left:
                    operator = operator.left
                    min_val = operator.new_node

                root.right = self.delete(root.right, root.new_node)

        return root

    def pre_order(self):
        print(self.new_node[0], self.new_node[1], end=', ')
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(self.new_node[0], self.new_node[1], end=', ')
        if self.right is not None:
            self.right.in_order() 

    def post_order(self): 
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.new_node[0], self.new_node[1], end=', ')

    def minimum(self):
        current = self.root
        while current.left is not None:
            current = current.left

        return current.username_construct, current.password_construct

    def maximum(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.username_construct, current.password_construct

    def print(self): 
        if self.left:
            self.left.print()

        print(self.new_node)
        if self.right:
            self.right.print()

binary_tree = BST(("ayaka", 69420))
print("Print out all nodes in BST:")
binary_tree.insert(('sasha', 34920))
binary_tree.insert(('kiki', 71649))
binary_tree.insert(('garfield', 89124))
binary_tree.insert(('sam', 16202))
binary_tree.insert(('cat', 46891))
binary_tree.insert(('lucy', 38456))
binary_tree.insert(('marie', 85557))
binary_tree.insert(('mimi', 33954))
binary_tree.insert(('diana', 97969))
binary_tree.insert(('muschi', 83318))
binary_tree.insert(('sugar', 74045))
binary_tree.insert(('millie', 25074))
binary_tree.insert(('ziggy', 65274))
binary_tree.print()

binary_tree.find(("ayaka", 69420))

# binary_tree.in_order()
# binary_tree.post_order()
binary_tree.pre_order()

print("Login system")
attempts = 0
while attempts <= 3:
    username_input = input('Enter username: ')
    password_input = int(input('Enter password: '))
    final = tuple([username_input, password_input])
    if final == ('sam', 16202):
        print("Login successfully")
        break
    else:
        print("Incorrect Password or Username")
        attempts += 1
        continue