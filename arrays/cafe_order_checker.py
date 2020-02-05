import unittest


# Check if we're serving orders first-come, first-served
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    take_out_orders_index, dine_in_orders_index, served_orders_index = 0, 0, 0
    num_served_orders = len(served_orders)
    num_take_out_orders = len(take_out_orders)
    num_dine_in_orders = len(dine_in_orders)

    while served_orders_index < num_served_orders:
        if take_out_orders_index < num_take_out_orders and served_orders[served_orders_index] == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1
        elif dine_in_orders_index < num_dine_in_orders and served_orders[served_orders_index] == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1
        else:
            return False
        served_orders_index += 1
    
     # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != num_dine_in_orders or take_out_orders_index != num_take_out_orders:
        return False
    
    return True

# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)


unittest.main(verbosity=2)
