class Node:
    """
    Create a new node for the binary search tree.

    Args:
        value (int): The value to be stored in the node
        parent (Node): The parent node of this node
        left_child (Node): left child of this node
        right_child (Node): right child of this node
    """
    def __init__(self, value=None, parent=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 1


class BinarySearchTree:
    """
    Create a new binary search tree.

    Args:
        values (list): A list of values to be added to the tree. Defaults to None
        root (Node): A root of the tree.  Defaults to None
    """
    def __init__(self, values = None):
        self.root = None
        if values is not None:
            for value in values:
                self.add_node(value)

    def find_min(self, node):
        """
        Returns:
            int: The minimum value in the tree.
        """
        return node.value if not node.left_child else self.find_min(node.left_child)

    def find_max(self, node):
        """
        Returns:
            int: The maximum value in the tree.
        """
        return node.value if not node.right_child else self.find_max(node.right_child)

    def add_node(self, val):
        """
        Adds a node to the tree.
        If no root -> sets up the root.
        """
        if self.root == None:
            self.root = Node(val)
        else:
            self._add_node(self.root, val)

    def _add_node(self, current_node, val):
        """
        Adds a node to it's spot inside a tree
        If it finds a spot, creates a node with a connection to its parent
        """
        if val < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(val, current_node)
            else:
                self._add_node(current_node.left_child, val)
        elif val > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(val, current_node)
            else:
                self._add_node(current_node.right_child, val)

    def find_node(self, val):
        """
        Finds a node by key
        """
        return self._find_node(self.root, val) if self.root else None

    def _find_node(self, current_node, val):
        """
        It goes deeper by recursion.
        When it finds the value or the node is equal to None - returns it
        """
        if current_node is None or val == current_node.value:
            return current_node
        elif val < current_node.value:
            return self._find_node(current_node.left_child, val)
        else:
            return self._find_node(current_node.right_child, val)

    def remove_node(self, val):
        """
        Depends on the case, it deletes a node by given value
        """
        node = self.find_node(val)
        if node is None:
            return
        if node.left_child is None or node.right_child is None:
            y=node
        else:
            y=self.find_successor(node)
        if y.left_child is not None:
            x=y.left_child
        else:
            x=y.right_child
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left_child:
                y.parent.left_child = x
            else:
                y.parent.right_child = x
        if y != node:
            node.value = y.value
        return y

    def find_successor(self, node):
        """
        It searches for the successor of the given node in the tree
        Useful when deleting node with both children
        """
        if node.right_child is not None:
            return self.find_node(self.find_min(node.right_child))
        node_tmp = node.parent
        while node_tmp is not None and node_tmp.left_child is not None:
            node = node_tmp
            node_tmp = node_tmp.parent
        return node_tmp

    def print_tree(self):
        """
        It prints the tree by rotating every younger node by 90 degrees
        """
        if self.root == None:
            return None
        print(f"Min value: {self.find_min(self.root)}")
        print(f"Max value: {self.find_max(self.root)}")
        self.print_node(self.root, 0, "")

    def print_node(self, current_node, indent, prefix):
        print(f"{' ' * indent}{prefix} {current_node.value}")
        if current_node.left_child:
            self.print_node(current_node.left_child, indent + 4, "L:")
        if current_node.right_child:
            self.print_node(current_node.right_child, indent + 4, "P:")