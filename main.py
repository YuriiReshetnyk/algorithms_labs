from Node import Node
from RedBlackTree import RedBlackTree


def main():
    new_red_black_tree = RedBlackTree()

    new_red_black_tree.root = Node(10)
    new_red_black_tree.root.left = new_red_black_tree.NULL
    new_red_black_tree.root.right = new_red_black_tree.NULL
    new_red_black_tree.root.color = 0

    new_red_black_tree.root.left = Node(5)
    new_red_black_tree.root.left.left = new_red_black_tree.NULL
    new_red_black_tree.root.left.right = new_red_black_tree.NULL
    new_red_black_tree.root.left.color = 1

    new_red_black_tree.print_tree()

    print("\n___________________________________________")
    new_red_black_tree.delete_node(10)
    new_red_black_tree.print_tree()


if __name__ == '__main__':
    main()
