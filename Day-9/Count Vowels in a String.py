def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
print(count_vowels("Hello World"))   # Output: 3 (o, o, and e)
