import unittest

# Find a number that appears more than once ... in O(n) time
def find_duplicate(int_list):

    ## Think of your list as a Linked list with each node A's value
    ## being the node that A's *next is pointing to. A duplicate will
    ## have two or more *next pointers pointing to it. Find that node
    ## with multiple arrows coming to it and thats your answer!
    
    ## However, we need O(1) space and Linked list uses O(n) extra space 
    ## to store pointers. We can avoid that by cycling throught the list 
    ## the following way
    n = len(int_list) - 1

    # Step 1: Get inside a cycle: Start at a position and walk n steps
    ## to find a position guaranteed to be in a cycle
    position_in_cycle = n+1 # head node of Linked list
    for _ in range(n): # 0 indexing vs 1 positioning
        position_in_cycle = int_list[position_in_cycle - 1] 
    
    # Step 2: Find the length of a cycle
    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = int_list[position_in_cycle-1]
    cycle_count = 1 # since we moved ahead by one position
    
    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle-1]
        cycle_count += 1

    # Step 3: Find the first node of a cycle using the head node and length
    # Use two pointers: One at head node, and the other at a node cycle_count 
    # away from head node
    pointer_start = n+1
    pointer_ahead = n+1
    
    ## walking through the linkedlist for cycle_couunt steps to place end 
    # node of stick approach
    for _ in range(cycle_count):
        pointer_ahead = int_list[pointer_ahead-1]
        
    ## Advance both pointers simultaneously until both pointers are at the same node:
    ## our node of interest!
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start-1]
        pointer_ahead = int_list[pointer_ahead-1]

    # Now both pointer_start and pointer_ahead are the same node (first node of the cycle)
    # and our duplicate

    return pointer_start


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)