import unittest

def is_valid_mine_initial(code):
    openers = set(('(','{', '['))
    closers = set((')','}', ']'))
    # Determine if the input code is valid
    java_code_opener_stack = []
    for char in code:
        if char in openers:
            java_code_opener_stack.append(char)
        if char in closers:
            if not java_code_opener_stack:
                return False
            prev_opener = java_code_opener_stack.pop()
            if ((char == ')' and prev_opener != '(') \
            or (char == '}' and prev_opener != '{') \
            or (char == ']' and prev_opener != '[')):
                return False
    if len(java_code_opener_stack) > 0:
        return False
    return True

## cleaned up code based on interview cake (Idea was right!)
def is_valid_standard(code):
    openers_to_closers = { 
        '(': ')',
        '{': '}', 
        '[':']', 
    }
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())
    
    # Determine if the input code is valid
    openers_stack = []
    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
            if not openers_to_closers[last_unclosed_opener] == char:
                return False
    return openers_stack == []


## cleaned up code based on interview cake (Idea was right!)
def is_valid(code):
    openers_to_closers = { 
        '(': ')',
        '{': '}', 
        '[':']',
        '|':'|',
    }
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())
    
    # Determine if the input code is valid
    openers_stack = []
    count = 0
    for char in code:
        if char == '|':
            count += 1
        if char in openers:
            if char != '|' or (char == '|' and count % 2 == 1):
                openers_stack.append(char)
        if char in closers:
            if char != '|' or (char == '|' and count % 2 == 0):
                if not openers_stack:
                    return False
                else:
                    last_unclosed_opener = openers_stack.pop()
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False
    return openers_stack == []


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_valid_longer_code_with_vert(self):
        result = is_valid('([]{|[]|})|[]{{}()}|')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
