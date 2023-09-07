def is_balanced(expression):
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    
    # Define strings for opening and closing brackets
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in opening_brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in closing_brackets:
            # Check if the stack is empty (no matching opening bracket)
            if not stack:
                return False  # No matching opening bracket found
            # Get the top element from the stack
            top = stack.pop()
            # Check if the closing bracket matches the top of the stack
            if char == ")" and top != "(" or char == "]" and top != "[" or char == "}" and top != "{":
                return False  # Mismatched closing bracket
    # After processing the entire expression, check if the stack is empty
    return not stack  # If stack is empty, expression is balanced

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
