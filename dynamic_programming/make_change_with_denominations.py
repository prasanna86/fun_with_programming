import unittest

# Calculate the number of ways to make change in a bottom up fashion
def change_possibilities(total_amount, denominations):
    # initializing an array of possibilities for each amount
    memo = [0] * (total_amount+1)
    memo[0] = 1 # number of ways to make zero
    
    for coin in denominations:
        for amount in range(coin, total_amount+1):
            amount_remainder = amount - coin
            memo[amount] += memo[amount_remainder]
    return memo[total_amount]
    
# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)