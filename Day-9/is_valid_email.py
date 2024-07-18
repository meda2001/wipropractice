import re

def is_valid_email(email):
    pattern = r'^[^@]+@[^@]+\.[^@]+$'
    return re.match(pattern, email) is not None

# Test
print(is_valid_email("example@example.com"))  # Output: True
print(is_valid_email("example.com"))          # Output: False
print(is_valid_email("example@.com"))         # Output: False
