import pytest
from bst import BinarySearchTree, Node

def test_create_bst_tree_empty():
    bst = BinarySearchTree()
    assert bst.root is None

def test_create_bst_tree_normal():
    bst = BinarySearchTree([4,2,6,7])
    assert bst.root.value == 4
    assert bst.root.left_child.value == 2
    assert bst.root.right_child.value == 6
    assert bst.root.right_child.left_child is None
    assert bst.root.right_child.right_child.value == 7

def test_create_bst_tree_normal_2():
    bst = BinarySearchTree([4,6,8,9])
    bst = BinarySearchTree([4,6,8,9])
    assert bst.root.value == 4
    assert bst.root.left_child is None
    assert bst.root.right_child.value == 6
    assert bst.root.right_child.left_child is None
    assert bst.root.right_child.right_child.value == 8
    assert bst.root.right_child.right_child.left_child is None
    assert bst.root.right_child.right_child.right_child.value == 9
    assert bst.root.right_child.right_child.right_child.left_child is None
    assert bst.root.right_child.right_child.right_child.right_child is None

def test_create_bst_tree_normal_2():
    bst = BinarySearchTree([2,5,0,1])
    assert bst.root.value == 2
    assert bst.root.left_child.value == 0
    assert bst.root.left_child.left_child is None
    assert bst.root.left_child.right_child.value == 1
    assert bst.root.right_child.value == 5
    assert bst.root.right_child.left_child is None
    assert bst.root.right_child.right_child is None
    assert bst.root.left_child.right_child.left_child is None
    assert bst.root.left_child.right_child.right_child is None

def test_create_bst_tree_sorted():
    bst = BinarySearchTree([1,2,3,4,5])
    assert bst.root.value == 1
    assert bst.root.right_child.value == 2
    assert bst.root.right_child.right_child.value == 3
    assert bst.root.right_child.right_child.right_child.value == 4
    assert bst.root.right_child.right_child.right_child.right_child.value == 5

def test_add_one_node():
    bst = BinarySearchTree()
    bst.add_node(5)
    assert bst.root.value == 5
    assert bst.root.left_child is None
    assert bst.root.right_child is None

def test_add_some_nodes():
    bst = BinarySearchTree()
    bst.add_node(5)
    bst.add_node(3)
    bst.add_node(1)
    bst.add_node(6)
    assert bst.root.value == 5
    assert bst.root.left_child.value == 3
    assert bst.root.right_child.value == 6
    assert bst.root.right_child.left_child is None
    assert bst.root.left_child.left_child.value == 1

def test_find_node_reqursion():
    bst = BinarySearchTree([5, 3, 7, 1])
    node = bst._find_node(bst.root, 3)
    assert node == bst.root.left_child

def test_find_node_reqursion_2():
    bst = BinarySearchTree([5, 3, 7, 1])
    node = bst._find_node(bst.root, 1)
    assert node == bst.root.left_child.left_child

def test_find_node_normal():
    bst = BinarySearchTree([5, 3, 7, 1])
    node = bst.find_node(7)
    assert node.value == 7

def test_find_node_not_in_tree():
    bst = BinarySearchTree([5, 3, 7, 1])
    node = bst.find_node(69)
    assert node is None

def test_remove_node_leaf():
    bst = BinarySearchTree([5, 3, 7, 1])
    assert bst.root.right_child.value == 7
    bst.remove_node(7)
    assert bst.root.right_child is None


def test_remove_node_not_leaf():
    bst = BinarySearchTree([5, 3, 7, 1])
    assert bst.root.left_child.value == 3
    assert bst.root.left_child.left_child is not None
    bst.remove_node(3)
    assert bst.root.left_child.value == 1
    assert bst.root.left_child.left_child is None

def test_remove_node_root():
    bst = BinarySearchTree([5, 3, 7, 1])
    assert bst.root.value == 5
    bst.remove_node(5)
    assert bst.root.value == 7

def test_find_successor():
    bst = BinarySearchTree([5, 3, 7, 1])
    tmp=bst.find_successor(bst.root.right_child)
    assert tmp is None
