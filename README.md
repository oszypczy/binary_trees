# Readme

This is a Python program that generates graphs to analyze the performance of Binary Search Trees (BSTs) and AVL Trees. The program uses the `matplotlib` library to plot the graphs.

## Prerequisites

Make sure you have the following installed before running the program:

- Python 3.x
- `matplotlib` library

## Getting Started

To run the program, follow these steps:

1. Clone the repository or download the source code files.
2. Open a terminal and navigate to the directory where the files are located.
3. Run the `main.py` file using the following command:

   ```
   python main.py
   ```

## Functionality

The program includes the following functions:

- `get_creation_graph_BST(numbers, title)`: Generates a graph showing the creation time of a Binary Search Tree for different collection sizes. The `numbers` parameter is a list of random integers, and the `title` parameter specifies the title of the graph.

- `get_creation_merged_graph_BST(numbers, title)`: Generates a merged graph comparing the creation time of a Binary Search Tree for both unsorted and sorted collections.

- `get_search_graph_BST(numbers, title)`: Generates a graph showing the search time of a Binary Search Tree for different collection sizes.

- `get_search_merged_graph_BST(numbers, title)`: Generates a merged graph comparing the search time of a Binary Search Tree for both unsorted and sorted collections.

- `get_remove_graph_BST(numbers, title)`: Generates a graph showing the remove time of a Binary Search Tree for different collection sizes.

- `get_remove_merged_graph_BST(numbers, title)`: Generates a merged graph comparing the remove time of a Binary Search Tree for both unsorted and sorted collections.

- `get_creation_graph_AVL(numbers, title)`: Generates a graph showing the creation time of an AVL Tree for different collection sizes.

- `get_search_graph_AVL(numbers, title)`: Generates a graph showing the search time of an AVL Tree for different collection sizes.

- `get_creation_merged_graph_BST_AVL(numbers, title)`: Generates a merged graph comparing the creation time of a Binary Search Tree and an AVL Tree for unsorted collections.

- `get_search_merged_graph_BST_AVL(numbers, title)`: Generates a merged graph comparing the search time of a Binary Search Tree and an AVL Tree for sorted collections.

## Usage

You can uncomment the function calls in the `main()` function to generate the desired graphs. By default, the program generates the following graphs:

- BST creation time graph
- BST search time graph
- BST remove time graph
- AVL creation time graph
- AVL search time graph
- BST vs AVL creation time merged graph (unsorted collections)
- BST vs AVL search time merged graph (sorted collections)

You can modify the `numbers` list to change the collection of numbers used for the graphs.

The generated graphs are saved in separate directories named `BST_plots` and `AVL_plots` for the BST and AVL trees, respectively. The merged graphs comparing BST and AVL trees are saved in the `BST_AVL_plots` directory.

## Contributing

If you want to contribute to this project, you can fork the repository and make any desired changes. You can also open issues for bug reports or feature requests.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify the code according to your needs.
