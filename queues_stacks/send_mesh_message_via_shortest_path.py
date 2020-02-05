
import unittest
from collections import deque

def reconstruct_path(how_we_reached_nodes, start_node, end_node):
    # Let your path be a list that you populate
    shortest_path = []
    # Start from the end of the path and work backwards
    current_node = end_node
    
    while current_node:
        shortest_path.append(current_node)
        current_node = how_we_reached_nodes[current_node]
    
    shortest_path.reverse()
    return shortest_path

# Find the shortest route in the network between the two users
def get_path(graph, start_node, end_node):
    
    if start_node not in graph:
        raise Exception("Start node not in graph!")
    if end_node not in graph:
        raise Exception("End node not in graph!")
        
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)
    
    # Keep track of how we got to each node
    # Useful to reconstruct shortest path
    how_we_reached_nodes = {start_node: None}
    
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()
        
        # stop when we reach the end node
        if current_node == end_node:
            # Found it!
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                # Keep track of how we got to this node
                how_we_reached_nodes[neighbor] = current_node
    
    # if we don't find a path
    return None

# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
