import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    m = len(my_list)
    n = len(alices_list)
    combined_list = [None] * (m+n)
    
    my_index = 0
    alice_index = 0
    combined_list_index = 0
    while(combined_list_index < m+n):
        is_my_list_exhausted = my_index >= m
        is_alices_list_exhausted = alice_index >= n
    
        if(not is_my_list_exhausted and (is_alices_list_exhausted or my_list[my_index] < alices_list[alice_index])):
            combined_list[combined_list_index] = my_list[my_index]
            my_index += 1
        else:
            combined_list[combined_list_index] = alices_list[alice_index]
            alice_index += 1
        
        combined_list_index += 1
    return combined_list

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
