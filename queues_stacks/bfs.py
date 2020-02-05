import unittest
from collections import deque

def bfs(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception("Start node not in graph!")
    
    if end_node not in graph:
        raise Exception("End node not in graph!")
    
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of what nodes we've already visited
    # so that we don't revisit them
    nodes_already_seen = set([start_node])
    
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()
        
        # stop when we reach the end node
        if current_node == end_node:
            # Found it!
            return True
        
        for neighbor in graph[current_node]:
            if neighbor not in nodes_already_seen:
                nodes_already_seen.add(neighbor)
                nodes_to_visit.append(neighbor)

    return False

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
        actual = bfs(self.graph, 'a', 'e')
        expected = True
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs(self.graph, 'd', 'c')
        expected = True
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs(self.graph, 'a', 'c')
        expected = True
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs(self.graph, 'f', 'g')
        expected = True
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs(self.graph, 'g', 'f')
        expected = True
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs(self.graph, 'a', 'a')
        expected = True
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs(self.graph, 'a', 'f')
        expected = False
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs(self.graph, 'a', 'h')


unittest.main(verbosity=2)
