def remove_duplicates(lst):
    return list(set(lst))

# Test
print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates([]))                        # Output: []
print(remove_duplicates([1, 1, 1, 1]))              # Output: [1]
