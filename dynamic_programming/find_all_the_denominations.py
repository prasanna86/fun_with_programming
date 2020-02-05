# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Example: 3, 4, 5 (candidate numbers), target 9
# (3,3,3) (4, 5) 

# find_candidates(9) = find_candidates(9-3) + find_candidates(9-4) + find_candidate(9-5)


# def find_all_candidates(target, candidates):
#     memo = [0] * (target+1)
#     memo[0] = 1

#     for item in candidates: # 3, 4, 5
#         for value in range(item, target+1): # 3, 4, 5, 6, 7, 8,9 
#             memo[value] += memo[value-item]
#     return memo[target]

# # recursion: sum, 
# 3 <  9
# 3 + 3 < 9
# 3+3+3 > 8
# 3+3+4 > 9
# def find_all_candidates(target, candidates):
#     solutions = []
#     for i, item in enumerate(candidates):
#         soln = []
# while(sum_items < target):
# sum_items += item
# soln.append(item)
# If sum_items == target:
# solutions.append(soln)
# elif sum_items > target:
# find_candidates_with_specific_candidate(target-item, candidates[i:,], i, solutions, soln)

#     return set(solutions)

# Def find_candidates_with_specific_candidate(amount,candidates, index, solutions, soln):
#     If amount == 0:
#         return solutions.append(soln)
#     Else:
#         amount -= candidates[index]
# find_candidates_with_specific_candidate(amount,candidates, index+1, solutions, soln)

import unittest

def combinationSum(candidates, target):
    all_solutions = []
    current_soln = []
    return build_solns_through_recursion(candidates, target, all_solutions, current_soln)

def build_solns_through_recursion(candidate_list, target_sum, solution_list, soln):
    for i in range(len(candidate_list)):
        soln.append(candidate_list[i])
            
        if (sum(soln) == target_sum):
            solution_list.append(soln[:])
            
        if (sum(soln) < target_sum):
            build_solns_through_recursion(candidate_list[i:], target_sum, solution_list, soln)

        soln.pop()

    return solution_list

# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = combinationSum([1, 2, 3], 4)
        expected = [[1,1,1,1],[1,1,2],[1,3],[2,2]]
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = combinationSum([1, 2], 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = combinationSum([], 1)
        expected = []
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = combinationSum([25, 50], 5)
        expected = []
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = combinationSum([5, 10], 50)
        expected = [[5,5,5,5,5,5,5,5,5,5],[5,5,5,5,5,5,5,5,10],[5,5,5,5,5,5,10,10],[5,5,5,5,10,10,10],[5,5,10,10,10,10],[10,10,10,10,10]]
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = combinationSum([1, 5, 7], 11)
        expected = [[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,5],[1,1,1,1,7],[1,5,5]]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

    
    

