import unittest
import math

## Building hash table for number of character occurences
def build_hash_table(input_string):
    table = {}
    for char in input_string:
        if char in table.keys():
            table[char] += 1
        else:
            table[char] = 1
    return table

## checking if permutation is a palindrome
def is_permutation_palindrome(input_string):

    table = build_hash_table(input_string)
    count_odd_counts = 0

    for value in table.values():
        if(value % 2 != 0):
            count_odd_counts += 1
    
    if(count_odd_counts > 1):
        return 0
    else:
        return 1

## counting number of permutations that are palindromes
def count_palindromes(input_string):

    table = build_hash_table(input_string)
    count_odd_counts = 0

    even_char_list = []
    for value in table.values():
        if(value % 2 != 0):
            count_odd_counts += 1
        else:
            even_char_list.append(value / 2)

    if(count_odd_counts > 1):
        return 0
    else:
        num_palindromes = math.factorial(sum(even_char_list))
        for val in even_char_list:
            num_palindromes /= math.factorial(val)
        return num_palindromes


# Tests

class Test(unittest.TestCase):
    
    def test_permutation_with_odd_number_of_chars(self):
        result = is_permutation_palindrome('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = is_permutation_palindrome('abbyya')
        self.assertTrue(result)
        
    def test_no_permutation_with_odd_number_of_chars(self):
        result = is_permutation_palindrome('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = is_permutation_palindrome('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_permutation_palindrome('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = is_permutation_palindrome('a')
        self.assertTrue(result)

    def test_count_permutations(self):
        result = count_palindromes('abbyya')
        self.assertEqual(result, 6)

unittest.main(verbosity=2)


