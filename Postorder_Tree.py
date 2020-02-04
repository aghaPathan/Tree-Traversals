
from Tree import Node

tree_order = []

# Creating a tree
root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.left_child.left_child.left_child = Node(8)
root.left_child.left_child.left_child.left_child = Node(9)
root.left_child.left_child.left_child.right_child = Node(10)


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


