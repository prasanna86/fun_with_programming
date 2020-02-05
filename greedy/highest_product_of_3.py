# Given a list of integers, find the highest product you can get from three of the integers.
# Assume the input list_of_ints will always have at least three integers.
import unittest


def highest_product_of_3_sorting(list_of_ints):

    # Calculate the highest product of three numbers
    sorted_ints = sorted(list_of_ints)
    neg_ints = [i for i in sorted_ints if i < 0]
    pos_ints = [i for i in sorted_ints if i >= 0]
    
    prod1 = sorted_ints[0] * sorted_ints[1] * sorted_ints[-1]
    prod2 = sorted_ints[-1] * sorted_ints[-2] * sorted_ints[-3]

    if(len(neg_ints) <= 1 or len(pos_ints) == 0):
        product = prod2
    elif(len(pos_ints) == 1):
        product = prod1
    else:
        product = max(prod1, prod2)

    return product

###############################################################
## Attempt at O(n) soln
def calculate_prod_neg_two_pos_max(numbers):
    lowest_index = numbers.index(min(numbers))
    a = numbers.pop(lowest_index)
    next_lowest_index = numbers.index(min(numbers))
    b = numbers.pop(next_lowest_index)
    highest_index = numbers.index(max(numbers))
    c = numbers.pop(highest_index)
    prod = a * b * c
    return prod
    
def calculate_prod_pos_three(numbers):
    highest_index = numbers.index(max(numbers))
    a = numbers.pop(highest_index)
    next_high_index = numbers.index(max(numbers))
    b = numbers.pop(next_high_index)
    third_high_index = numbers.index(max(numbers))
    c = numbers.pop(third_high_index)
    prod = a * b * c
    return prod

def highest_product_of_3_n_soln_attempt(list_of_ints):
    neg_ints = [i for i in list_of_ints if i < 0]
    pos_ints = [i for i in list_of_ints if i >= 0]
    
    numbers = list_of_ints
    prod1 = calculate_prod_neg_two_pos_max(numbers)
    numbers = list_of_ints
    prod2 = calculate_prod_pos_three(numbers)
    
    if len(neg_ints) <= 1 or len(pos_ints) == 0:
        prod = prod2
    elif len(pos_ints) == 1:
        prod = prod1
    else:
        prod = max(prod1, prod2)
    return prod

###########################################################
# Calculate the highest product of three numbers
def highest_product_of_3(list_of_ints):
    n = len(list_of_ints)

    ## less than 3 ints, throw exception
    if n < 3:
        raise ValueError('less than 3 integers!')
         
    # initializing
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    # Walk through the list starting at index 2
    for i in range(2, n):
        current = list_of_ints[i]
        # check if we have a new highest product of 3
        highest_product_of_3 = max(highest_product_of_3, 
                                  current * highest_product_of_2,
                                  current * lowest_product_of_2)
                                   
        # update highest_product_of_2
        highest_product_of_2 = max(highest_product_of_2,
                                  current * highest,
                                  current * lowest)
        # lowest product of 2
        lowest_product_of_2 = min(lowest_product_of_2,
                                 current * highest,
                                 current * lowest)
                                     
        # highest
        highest = max(highest, current)
        # lowest
        lowest = min(lowest, current)
        
    return highest_product_of_3


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])

unittest.main(verbosity=2)
