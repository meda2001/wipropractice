def sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

# Test
print(sum_of_evens([1, 2, 3, 4, 5, 6]))  # Output: 12
print(sum_of_evens([7, 8, 10, 13]))      # Output: 18
print(sum_of_evens([1, 3, 5, 7]))        # Output: 0
