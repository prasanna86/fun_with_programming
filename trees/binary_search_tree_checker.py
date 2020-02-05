import unittest


# Determine if the tree is a valid binary search tree
def is_binary_search_tree2(root):
    vals = []
    in_order_traversal(root, vals)
    for i in range(len(vals)-1):
        if vals[i] > vals[i+1]:
            return False
    return True

def in_order_traversal(node, vals):
    if node.left:
        in_order_traversal(node.left, vals)
    vals.append(node.value)
    if node.right:
        in_order_traversal(node.right, vals)
    return

def is_binary_search_tree(root):
    # keep adding nodes along with what it 
    # needs to be compared against
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]
    
    ## Do DFS
    while(len(node_and_bounds_stack)):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        
        ## check validity of node in terms whether 
        ## its at the right place in the tree
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False
        
        
        ## Check for children: Add a new left or right node
        
        # the left node needs to be compared with current node value
        if node.left: 
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right: 
            node_and_bounds_stack.append((node.right, node.value, upper_bound))
    ## In case we get here after visiting all nodes
    return True

# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)