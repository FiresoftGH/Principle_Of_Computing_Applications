class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, item):
        if not self.val:
            self.val = item
            return

        if self.val == item:
            return

        if item < self.val:
            if self.left:
                self.left.insert(item)
                return

            else:
                self.left = BSTNode(item)

        if item > self.val:
            if self.right:
                self.right.insert(item)
                return

            else:
                self.right = BSTNode(item)

    def delete(self, val):
        if not self.val:
            return self

        elif val < self.val:
            self.left = self.left.delete(val)
            return self

        elif val > self.val:
            self.left = self.right.delete(val)
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

    def exists(self, val):
        if self.val == val:
            return True

        if val < self.val:
            if self.left is None:
                return False

            else:
                return self.left.exists(val)

        if self.right is None:
            return False

        else:
            return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)

        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.inorder(vals)

        return self

    def postorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)

        if self.right is not None:
            self.right.inorder(vals)

        if self.val is not None:
            vals.append(self.val)

        return self

test = BSTNode()

test.insert(1)
test.insert(2)
test.insert(3)

print(test.exists(2))
print(test.preorder([]))