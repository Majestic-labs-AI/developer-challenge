"""
    This is a weird other way to do this that I came up with and think is cool...
    - I noticed that this "in-order traverse" is the same as just reading the tree left to right when you draw it out,
        so it makes sense that we could get an ordered list by just "collapsing" the tree down onto the x-axis (makes 
        sense visually)
    - The code below does this by finding the corresponding position (on a sufficiently large vector, v) of each node,
        going down from the parent node.
    - The result is a length 2^(N) - 1 vector, where N = number of nodes created, and the not-None values are the nodes
        of the tree in the order of the in-order traverse from the exercise.
    - While we can obviously just return the not-None values to get the desired result, the full vector is interesting
        because it describes only one distinct tree, as certain positions of the vector are only accessible at certain
        "levels" of the tree. 
"""

class Node:
    # Total number of nodes
    count = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        Node.count += 1
    
    @staticmethod
    def midpoint():
        """Get the midpoint of the max width tree"""

        return 2 ** (Node.count - 1) - 1

    def traverse(self, v, p, c, mid):
        """Traverse the tree, filling the vector `v`."""

        # print(f"Depth level {c}, Node: {self.data}, Going in Position: {p}")
        v[p] = self.data

        # Traverse the left child if it exists
        if self.left:
            newp = p - (mid + 1) // (2 ** c)
            self.left.traverse(v, newp, c + 1, mid)

        # Traverse the right child if it exists
        if self.right:
            newp = p + (mid + 1) // (2 ** c)
            self.right.traverse(v, newp, c + 1, mid)


def main():
    # Create nodes and initialize the tree
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    # Initialize the tree structure
    a.left = b
    b.left = d
    b.right = e
    a.right = c
    c.left = f
    c.right = g

    mid = Node.midpoint()

    # Empty vector to be filled with ordered nodes
    v = [None] * (mid * 2)

    # Traverse
    a.traverse(v=v, p=mid, c=1, mid=mid)

    # Remove None values to view clean, ordered list
    v_filtered = [item for item in v if item is not None]

    print("\nClean Answer: \n\n", v_filtered)
    print("\n------------------------------------------------------------------------\n")
    print("Full, Fun Vector: \n\n", v, "\n")


if __name__ == "__main__":
    main()
