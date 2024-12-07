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
    # Create nodes and initialize the tree
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    j = Node('j')

    # Initialize the tree structure
    a.left = b
    b.left = d
    b.right = e
    e.left = g
    e.right = h
    a.right = c
    c.left = f
    f.left = i
    i.right = j

    # Traverse and print the tree
    a.traverse()


if __name__ == "__main__":
    main()
