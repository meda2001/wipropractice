


def calculate(expression):
    return eval(expression)

# Example usage:
s = "1 + 1"
print(calculate(s))  # Output: 2

s = " 2-1 + 2 "
print(calculate(s))  # Output: 3

s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))  # Output: 23
