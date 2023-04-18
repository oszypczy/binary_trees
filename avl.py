# Create a tree node
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

class AVLTree:
    # Constructor to create AVL tree from a list of values
    def __init__(self, values=[]):
        self.root = None
        for value in values:
            self.root = self.insert_node(self.root, value)

    # Function to insert a node
    def insert_node(self, root, value):
        # Check if the value already exists in the tree
        if root and root.value == value:
            return root
        # Find the correct location and insert the node
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left_child = self.insert_node(root.left_child, value)
        else:
            root.right_child = self.insert_node(root.right_child, value)

        root.height = 1 + max(self.getHeight(root.left_child), self.getHeight(root.right_child))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if value < root.left_child.value:
                return self.right_childRotate(root)
            else:
                root.left_child = self.left_childRotate(root.left_child)
                return self.right_childRotate(root)
        if balanceFactor < -1:
            if value > root.right_child.value:
                return self.left_childRotate(root)
            else:
                root.right_child = self.right_childRotate(root.right_child)
                return self.left_childRotate(root)
        return root

    # Function to perform left_child rotation
    def left_childRotate(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self.getHeight(z.left_child), self.getHeight(z.right_child))
        y.height = 1 + max(self.getHeight(y.left_child), self.getHeight(y.right_child))
        return y

    # Function to perform right_child rotation
    def right_childRotate(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.height = 1 + max(self.getHeight(z.left_child), self.getHeight(z.right_child))
        y.height = 1 + max(self.getHeight(y.left_child), self.getHeight(y.right_child))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left_child) - self.getHeight(root.right_child)

    def find_node(self, val):
        return self._find_node(self.root, val) if self.root else None

    def _find_node(self, current_node, val):
        if current_node is None or val == current_node.value:
            return current_node
        elif val < current_node.value:
            return self._find_node(current_node.left_child, val)
        else:
            return self._find_node(current_node.right_child, val)

    def print_tree(self):
        if self.root == None:
            return None
        self.print_node(self.root, 0, "")

    def print_node(self, current_node, indent, prefix):
        print(f"{' ' * indent}{prefix} {current_node.value}")
        if current_node.left_child:
            self.print_node(current_node.left_child, indent + 4, "L:")
        if current_node.right_child:
            self.print_node(current_node.right_child, indent + 4, "P:")
