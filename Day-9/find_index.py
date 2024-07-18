def find_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

# Test
print(find_index([1, 2, 3, 4, 5], 3))  # Output: 2
print(find_index([1, 2, 3, 4, 5], 6))  # Output: -1
print(find_index([], 1))               # Output: -1
