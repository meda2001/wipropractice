def second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second

# Test
print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # Output: 6
print(second_largest([10]))                     # Output: None
print(second_largest([10, 10, 10]))             # Output: None
