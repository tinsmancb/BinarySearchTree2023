class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class.
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newLeft):
            self.left = newLeft

        def setRight(self, newRight):
            self.right = newRight

        # Insert something into the tree.
        def insert(self, val):
            pass

        # Check if a value is in the tree.
        def contains(self, val):
            pass

        # Return all the items in the tree as a sorted list.
        def toList(self):
            pass

    def __init__(self):
        self.root = None

    # Insert something into the tree.
    def insert(self, val):
        if self.root is None:
            self.root = self.__Node(val)
        else:
            self.root.insert(val)

    # Check if a value is in the tree.
    def contains(self, val):
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    # Return all the items in the tree as a sorted list.
    def toList(self):
        if self.root is None:
            return []
        else:
            return self.root.toList()

def main():
    s = input("Enter a list of numbers, seperated by spaces: ")
    lst = s.split()

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))

    print(tree.toList())


if __name__ == "__main__":
    main()