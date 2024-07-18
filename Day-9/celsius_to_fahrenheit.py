def find_min(lst):
    if not lst:  # Handle empty list case
        return None
    return min(lst)

# Test case
print(find_min([4, 2, 9, 1]))  # Output: 1
print(find_min([]))  # Output: None
