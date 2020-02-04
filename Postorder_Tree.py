
from Tree import Node

tree_order = []

# Creating a tree
root = Node(25)
root.left_child = Node(15)
root.left_child.left_child = Node(10)
root.left_child.right_child = Node(22)
root.left_child.left_child.left_child = Node(4)
root.left_child.left_child.right_child = Node(12)
root.left_child.right_child.left_child = Node(18)
root.left_child.right_child.right_child = Node(24)
root.right_child = Node(50)
root.right_child.left_child = Node(35)
root.right_child.right_child = Node(70)
root.right_child.left_child.left_child = Node(31)
root.right_child.left_child.right_child = Node(44)
root.right_child.right_child.left_child = Node(66)
root.right_child.right_child.right_child = Node(90)

class In_Order():
    def __init__(self, root):
        """
            This class is used to demonstrate Post-Order Tree Traversal
        """
        self.tree_order = []
        self._process(root)

    def _process(self, root):
        """ This method processes the logic """
        if root:
            self._process(root.left_child)
            self._process(root.right_child)
            self.tree_order.append(root.node_data)


in_order_tree = In_Order(root)
# Printing Tree Order
print(in_order_tree.tree_order)


