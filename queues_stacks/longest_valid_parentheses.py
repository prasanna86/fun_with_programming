class Solution:
    # O(n) time, O(n) space
    # Algorithm: Use a stack. keep track of indices of open 
    # brackets or index when stack is empty. Pop the stack when there's a matching
    # closer. Update max length comparing current max length with i - stack[-1]
    def longestValidParentheses(self, s: str):
        stack = []
        max_length = 0
        stack.append(-1)
        for i, char in enumerate(s):
            if char == '(':
                # keep track of the indices, not the character itself
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    if i-stack[-1] > max_length:
                        output = s[stack[-1]+1:i+1]
                        max_length = i-stack[-1]
        return output, max_length
    
    # O(n) time, O(1) space.
    # Algorithm: keep track of number of left and right brackets, 
    # scan them both ways, zero the brackets out whenever right becomes larger 
    # than left going one way, and when left becomes larger than right going 
    # backward, updating max_length all the time.
    def longestValidParentheses_constant_space(self, s: str) -> int:
        # counting number of left brackets and right brackets
        left, right, max_length = 0, 0, 0 
        for char in s:
            if char == '(': # keep track of left bracket counts
                left += 1
            else: # keep track of right bracket counts
                right += 1
        
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0
        return max_length