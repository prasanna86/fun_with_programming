import unittest

def max_duffel_bag_value(cake_tuples, weight_capacity):
    # List to hold the maximum possible value at every
    # integer capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)
    
    for current_capacity in range(weight_capacity+1):
        
        current_max_value = 0
        
        for cake_weight, cake_value in cake_tuples:
            # if the cake weighs as much or less than 
            # the current capacity, see what our max value
            # could be if we took it!
            if cake_weight == 0 and cake_value > 0:
                return float("inf")
            if cake_weight > 0 and cake_weight <= current_capacity and cake_value > 0:
                # Find max_value_using_cake
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity-cake_weight]

                current_max_value = max(max_value_using_cake, current_max_value)

        max_values_at_capacities[current_capacity] = current_max_value
    
    return max_values_at_capacities[weight_capacity]

    # Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)