class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traverse(self):
        # In-order traversal: Left -> Root -> Right
        if self.left:
            self.left.traverse()  # Traverse left subtree
        print(self.data, end=" ")  # Visit the current node
        if self.right:
            self.right.traverse()  # Traverse right subtree


def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    # Initialize the tree
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    # Traverse and print the tree
    a.traverse()


if __name__ == "__main__":
    main()
