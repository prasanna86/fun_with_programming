import unittest
import math
import numpy as np

def hash_scores(scores_list, max_score):
    hash_array = [0] * (max_score+1)

    for score in scores_list:
        hash_array[score] += 1

    return hash_array

def sort_scores(scores_list, max_score):

    hash_array = hash_scores(scores_list, max_score)
    sorted_scores = []

    for i in range(max_score, -1, -1):
        if(hash_array[i] > 0):
            for j in range(hash_array[i]):
                sorted_scores.append(i)

    return sorted_scores
        
# Tests
class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)

    def test_random_simulation_20_scores(self):
        n = 20
        scores_list = [np.random.randint(0, 100) for i in range(n)]

        actual = sort_scores(scores_list, 100)
        expected = sorted(scores_list, reverse=True)

        self.assertEqual(actual, expected)

    def test_random_simulation_100_scores(self):
        n = 100 
        scores_list = [np.random.randint(0, 100) for i in range(n)]

        actual = sort_scores(scores_list, 100)
        expected = sorted(scores_list, reverse=True)

        self.assertEqual(actual, expected)

    def test_random_simulation_random_number_of_scores(self):
        n = np.random.randint(0, 1000)
        scores_list = [np.random.randint(0, 100) for i in range(n)]

        actual = sort_scores(scores_list, 100)
        expected = sorted(scores_list, reverse=True)

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
        

    
