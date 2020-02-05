import unittest


# Implement methods to track the max, min, mean, and mode
class TempTracker(object):
    def __init__(self):
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.num_temps = 0
        self.num_occurrences = [0] * 111
        self.mean_temp = None
        self.mode_temp = None
    
    def insert(self, temperature):
        if temperature < self.min_temp:
            self.min_temp = temperature
        if temperature > self.max_temp:
            self.max_temp = temperature
    
        self.num_temps = self.num_temps + 1
        (self.num_occurrences)[temperature] += 1
        
        if self.num_temps > 1:
            self.mean_temp = ((self.mean_temp * (self.num_temps-1)) + temperature) / (self.num_temps)
            self.mode_temp = (self.num_occurrences).index(max(self.num_occurrences))
        else:
            self.mean_temp = temperature
            self.mode_temp = temperature
        
    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean_temp

    def get_mode(self):
        return self.mode_temp

# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)
