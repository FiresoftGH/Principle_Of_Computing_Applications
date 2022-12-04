# Reference: https://blog.boot.dev/computer-science/binary-search-tree-in-python/
import random as rd
# Create the binary search tree node class
class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    # Insert something into the BST
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    # Get the maximum value of the BST
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self is None:
            return self

        if val < self.val:
            self.left = self.left.delete(val)
            return self

        if val > self.val:
            self.right = self.right.delete(val)
            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    # Check if a variable exists within the class or not
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)
    
    # Inorder printing mode
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)

        if self.val is not None:
            vals.append(self.val)
        
        if self.right is not None:
            self.right.inorder(vals)

        return vals

    # Preorder printing mode
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)

        if self.left is not None:
            self.left.preorder(vals)

        if self.right is not None:
            self.right.preorder(vals)

        return vals

    # Postorder printing mode
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)

        if self.right is not None:
            self.right.postorder(vals)

        if self.val is not None:
            vals.append(self.val)

        return vals            

test = BSTNode()
test.insert(2)

for x in range(6):
    val = rd.randint(-100, 100)
    print(val)
    test.insert(val)

print(test.get_min())
print(test.preorder([]))
print(test.postorder([]))
print(test.inorder([]))

test.delete(2)
print(test.preorder([]))
print(test.postorder([]))
print(test.inorder([]))

# while True:
#     remove = int(input("Remove what?: "))
#     test.delete(remove)
#     print(test.preorder([]))
#     print(test.postorder([]))
#     print(test.inorder([]))



