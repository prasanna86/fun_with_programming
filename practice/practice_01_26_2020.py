# Can you see me typing?
#  Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

# You can assume the input string only contains lowercase letters.

# Examples:

#     "civic" should return True
#     "ivicc" should return True
#     "civil" should return False
#     "livci" should return False
from itertools import permutations

def is_string_a_palindrome(s):
  begin, end = 0, len(s)-1
  while(begin < end):
    if s[begin] != s[end]:
      return False
    begin +=1
    end -= 1
  return True

# O(n! n) algorithm
def is_any_permutation_palindrome_brute(s):
  if len(s) == 0:
    return True
  # algo: 1. list all permutations
  #				2. for each permutation, return true / false
  for p in permutations(s): # non repeated
    if is_string_a_palindrome(p):
      return True
  return False

# lookup defaultdict
def character_counts(s):
  counts = dict()
  for char in s.lower():
    if char not in counts:
      counts[char] = 1
    else:
    	counts[char] += 1
  return counts

def is_any_permutation_palindrome(s):
  counts = character_counts(s)
  number_of_odd_counts = 0
  for value in counts.values():
    if value % 2 == 1:
      number_of_odd_counts += 1
  return number_of_odd_counts <= 1


# c : 2
# i: 2
# v: 2

# abcbac: abccba (True)
# abccda: (False) a: 2, b: 1, c:2, d: 1
# abc, a: 1, b: 1, c: 1
# civic: c: 2, i: 2, v: 1
# civil: c: 1, i:2, v: 1, l: 1
# '': empty table, default True
# 'a': a: 1
# upper case, lower case

# -------------------------------------------------------
# You're working with an intern that keeps coming to you with JavaScript code that
# won't run because the braces, brackets, and parentheses are off. To save you both
# some time, you decide to write a braces/brackets/parentheses validator.

# #
# Let's say:

#     '(', '{', '[' are called "openers."
#     ')', '}', ']' are called "closers."

# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

# Examples:

#     "{ [ ] ( ) }" should return True
#     "{ [ ( ] ) }" should return False
#     "{ [ }" should return False
