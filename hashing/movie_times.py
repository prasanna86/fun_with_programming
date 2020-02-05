import unittest
import numpy as np

def build_hash_table(movie_times_list):
    table = {}
    for t in movie_times_list:
        if t in table.keys():
            table[t] += 1
        else:
            table[t] = 1
    return table

def has_two_movie_times(movie_times_list, flight_length):

    table = build_hash_table(movie_times_list)

    for t in table.keys():
        if flight_length-t in table.keys():
            if flight_length-t == (flight_length / 2) and table[flight_length-t] == 1:
                return 0
            return 1

def has_two_movie_times_sorting(movie_lengths, flight_length):
    sorted_movie_lengths = sorted(movie_lengths)
    start = 0
    end = len(movie_lengths)-1
    while(start < end):
        if(sorted_movie_lengths[start] + sorted_movie_lengths[end] == flight_length):
            return True
        elif(sorted_movie_lengths[start] + sorted_movie_lengths[end] > flight_length):
            end = end - 1
        else:
            start = start + 1
    return False

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = has_two_movie_times([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = has_two_movie_times([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = has_two_movie_times([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = has_two_movie_times([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = has_two_movie_times([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = has_two_movie_times([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = has_two_movie_times([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = has_two_movie_times([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
    
