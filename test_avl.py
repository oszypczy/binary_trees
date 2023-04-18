import pytest
from avl import AVLTree, TreeNode

def test_create_avl_tree_empty():
    avl = AVLTree()
    assert avl.root is None

def test_create_avl_tree_normal():
    avl = AVLTree([4,2,6,7])
    assert avl.root.value == 4
    assert avl.root.left_child.value == 2
    assert avl.root.right_child.value == 6
    assert avl.root.right_child.left_child is None
    assert avl.root.right_child.right_child.value == 7

def test_create_avl_tree_normal_2():
    avl = AVLTree([4,6,8,9])
    assert avl.root.value == 6
    assert avl.root.left_child.value == 4
    assert avl.root.right_child.value == 8
    assert avl.root.right_child.left_child is None
    assert avl.root.right_child.right_child.value == 9
    assert avl.root.right_child.right_child.left_child is None
    assert avl.root.right_child.right_child.right_child is None

def test_create_avl_tree_normal_3():
    avl = AVLTree([2,5,0,1])
    assert avl.root.value == 2
    assert avl.root.left_child.value == 0
    assert avl.root.left_child.left_child is None
    assert avl.root.left_child.right_child.value == 1
    assert avl.root.right_child.value == 5
    assert avl.root.right_child.left_child is None
    assert avl.root.right_child.right_child is None
    assert avl.root.left_child.right_child.left_child is None
    assert avl.root.left_child.right_child.right_child is None

def test_create_avl_tree_sorted():
    avl = AVLTree([1,2,3,4,5])
    assert avl.root.value == 2
    assert avl.root.right_child.value == 4
    assert avl.root.left_child.value == 1
    assert avl.root.right_child.right_child.value == 5
    assert avl.root.right_child.left_child.value == 3


def test_insert_one_node():
    avl = AVLTree()
    avl.root = avl.insert_node(avl.root, 5)
    avl.root.height
    assert avl.root.value == 5
    assert avl.root.left_child is None
    assert avl.root.right_child is None

def test_insert_some_nodes_and_height():
    avl = AVLTree()
    avl.root = avl.insert_node(avl.root, 5)
    assert avl.root.height == 1
    avl.insert_node(avl.root,3)
    avl.insert_node(avl.root,6)
    avl.insert_node(avl.root,2)
    assert avl.root.height == 3
    assert avl.root.value == 5
    assert avl.root.left_child.value == 3
    assert avl.root.right_child.value == 6
    assert avl.root.left_child.left_child.value == 2
    assert avl.root.left_child.right_child is None

def test_find_node_reqursion():
    avl = AVLTree([5, 3, 7, 1])
    node = avl._find_node(avl.root, 3)
    assert node == avl.root.left_child

def test_find_node_reqursion_2():
    avl = AVLTree([5, 3, 7, 1])
    node = avl._find_node(avl.root, 1)
    assert node == avl.root.left_child.left_child

def test_find_node_normal():
    avl = AVLTree([5, 3, 7, 1])
    node = avl.find_node(7)
    assert node.value == 7

def test_find_node_not_in_tree():
    avl = AVLTree([5, 3, 7, 1])
    node = avl.find_node(6)
    assert node is None

def test_getHeight():
    avl = AVLTree([5, 3, 7, 1])
    assert avl.getHeight(avl.root) == 3

def test_getHeight_v2():
    avl = AVLTree([5, 3, 7, 1,11,15,17,12,10,2,8])
    assert avl.getHeight(avl.root) == 4

def test_getHeight_sorted():
    avl = AVLTree([_ for _ in range(10)])
    assert avl.getHeight(avl.root) == 4

def test_getBalance():
    avl = AVLTree([_ for _ in range(10)])
    assert avl.getBalance(avl.root) == -1

def test_getBalance_left_child():
    avl = AVLTree([5, 3, 7, 1])
    assert avl.getBalance(avl.root.left_child) == 1

def test_getBalance_sorted():
    avl = AVLTree([1,2,3,5,8,10])
    assert avl.getBalance(avl.root.left_child) == 0

def test_getBalance_sorted_v2():
    avl = AVLTree([(_ + 1) for _ in range(10)])
    assert avl.getBalance(avl.root) == -1
