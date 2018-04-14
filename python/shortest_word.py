'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''
def find_short(s):
    return min([len(x) for x in s.split()]) # shortest word length