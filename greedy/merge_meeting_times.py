## O(nlogn) time and O(n) space
## Approach: Greedy - Sort first and then scan once
## Variant: With an upper bound, can this be faster?

import unittest

# Merge meeting ranges
def merge_ranges(meetings):

    ## Sort b start time
    sorted_meetings = sorted(meetings)
    
    # Initialize merged meetings by first tuple
    merged_meetings = [sorted_meetings[0]]
    
    n = len(sorted_meetings)
    for i in range(1, n):
        prev_merged_meeting = merged_meetings[-1]
        current_meeting = sorted_meetings[i]
    
        if(current_meeting[0] > prev_merged_meeting[1]):
            merged_meetings.append(current_meeting)
        else: # current meeting[0] <= prev_meeting[1]
            merged_meetings[-1] = (prev_merged_meeting[0], max(current_meeting[1], prev_merged_meeting[1]))

    return merged_meetings

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
