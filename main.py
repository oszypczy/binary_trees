from bst import BinarySearchTree
from avl import AVLTree
import random
import time
import gc
from matplotlib import pyplot as plt
import sys
import os

def get_creation_graph_BST(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = BinarySearchTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis.append(stop - start)
    plt.plot(x_axis, y_axis, '-')
    plt.title(label='BST creation time graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_creation_merged_graph_BST(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y1_axis = []
    y2_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = BinarySearchTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y1_axis.append(stop - start)
    numbers.sort()
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = BinarySearchTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y2_axis.append(stop - start)
    plt.plot(x_axis, y1_axis, '-', label="Unsorted collection")
    plt.plot(x_axis, y2_axis, '-', label="Sorted collection")
    plt.title(label='BST creation time merged graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.legend()
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_search_graph_BST(numbers, title):
    tree = BinarySearchTree(numbers)
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis.append(stop - start)
    plt.plot(x_axis, y_axis, '-')
    plt.title(label='BST search time graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_search_merged_graph_BST(numbers, title):
    tree1 = BinarySearchTree(numbers)
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y1_axis = []
    y2_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree1.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y1_axis.append(stop - start)
    numbers.sort()
    tree2 = BinarySearchTree(numbers)
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree2.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y2_axis.append(stop - start)
    plt.plot(x_axis, y1_axis, '-', label="Unsorted collection")
    plt.plot(x_axis, y2_axis, '-', label="Sorted collection")
    plt.title(label='BST search time merged graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.legend()
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_remove_graph_BST(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y_axis = []
    for range in x_axis:
        tree = BinarySearchTree(numbers)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree.remove_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis.append(stop - start)
    plt.plot(x_axis, y_axis, '-')
    plt.title(label='BST remove time graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_remove_merged_graph_BST(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y1_axis = []
    y2_axis = []
    for range in x_axis:
        tree1 = BinarySearchTree(numbers)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree1.remove_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y1_axis.append(stop - start)
    numbers.sort()
    for range in x_axis:
        tree2 = BinarySearchTree(numbers)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree2.remove_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y2_axis.append(stop - start)
    plt.plot(x_axis, y1_axis, '-', label="Unsorted collection")
    plt.plot(x_axis, y2_axis, '-', label="Sorted collection")
    plt.title(label='BST remove time merged graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.legend()
    plt.grid(True)
    if not os.path.exists('BST_plots'):
        os.makedirs('BST_plots')
    plt.savefig(os.path.join('BST_plots', title))

def get_creation_graph_AVL(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = AVLTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis.append(stop - start)
    plt.plot(x_axis, y_axis, '-')
    plt.title(label='AVL creation time graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('AVL_plots'):
        os.makedirs('AVL_plots')
    plt.savefig(os.path.join('AVL_plots', title))

def get_search_graph_AVL(numbers, title):
    tree = AVLTree(numbers)
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis.append(stop - start)
    plt.plot(x_axis, y_axis, '-')
    plt.title(label='AVL search time graph')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('AVL_plots'):
        os.makedirs('AVL_plots')
    plt.savefig(os.path.join('AVL_plots', title))

def get_creation_merged_graph_BST_AVL(numbers, title):
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y1_axis = []
    y2_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = BinarySearchTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y1_axis.append(stop - start)
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        tree = AVLTree(numbers[:range])
        stop = time.process_time()
        if gc_old: gc.enable()
        y2_axis.append(stop - start)
    plt.plot(x_axis, y1_axis, '-', label="BST tree")
    plt.plot(x_axis, y2_axis, '-', label="AVL tree")
    plt.title(label='BST vs AVL creation time merged graph - unsorted collections')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.legend()
    plt.grid(True)
    if not os.path.exists('BST_AVL_plots'):
        os.makedirs('BST_AVL_plots')
    plt.savefig(os.path.join('BST_AVL_plots', title))

def get_search_merged_graph_BST_AVL(numbers, title):
    tree1 = BinarySearchTree(numbers)
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y1_axis = []
    y2_axis = []
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree1.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y1_axis.append(stop - start)
    tree2 = AVLTree(numbers)
    for range in x_axis:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]:
            tree2.find_node(n)
        stop = time.process_time()
        if gc_old: gc.enable()
        y2_axis.append(stop - start)
    plt.plot(x_axis, y1_axis, '-', label="BST tree")
    plt.plot(x_axis, y2_axis, '-', label="AVL tree")
    plt.title(label='BST vs AVL search time merged graph - sorted collections')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.legend()
    plt.grid(True)
    if not os.path.exists('BST_AVL_plots'):
        os.makedirs('BST_AVL_plots')
    plt.savefig(os.path.join('BST_AVL_plots', title))

def main():
    sys.setrecursionlimit(10000)
    numbers = [random.randint(1, 30000) for _ in range(10000)]
    # numbers.sort()
    # get_creation_merged_graph_BST(numbers, "BST_merged_creation_time.png")
    # get_creation_graph_BST(numbers, "BST_average_creation_time.png")
    # get_creation_graph_BST(numbers, "BST_worst_case_creation_time.png")
    # get_search_graph_BST(numbers, "BST_average_search_time.png")
    # get_search_graph_BST(numbers, "BST_worst_case_search_time.png")
    # get_search_merged_graph_BST(numbers, "BST_merged_search_time.png")
    # get_remove_graph_BST(numbers, "BST_average_remove_time.png")
    # get_remove_graph_BST(numbers, "BST_worst_case_remove_time.png")
    # get_remove_merged_graph_BST(numbers, "BST_merged_remove_time.png")
    # get_creation_graph_AVL(numbers, "AVL_creation_time.png")
    # get_search_graph_AVL(numbers, "AVL_search_time.png")
    # get_creation_merged_graph_BST_AVL(numbers, "AVL_BST_unsorted_creation_time.png")
    # get_search_merged_graph_BST_AVL(numbers, "AVL_BST_sorted_search_time.png")
    tree = AVLTree([10,3,15,12,18,13])
    tree.print_tree()

if __name__ == "__main__":
    main()
