import unittest


def get_permutations(string):
    set_of_perms = []
    # Generate all permutations of the input string
    if len(string) == 0:
        set_of_perms.append('')
        return set(set_of_perms)

    ch = string[0]
    substring = string[1:]
    set_of_perms_substring = get_permutations(substring)
    for perm in set_of_perms_substring:
        set_of_perms.append(ch + perm)
        for j in range(len(perm)):
            set_of_perms.append(perm[0:j] + ch + perm[j:])
        set_of_perms.append(perm + ch)
    return set(set_of_perms)

# Tests
class Test(unittest.TestCase):
    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
