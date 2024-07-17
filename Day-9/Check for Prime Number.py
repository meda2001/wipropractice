def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Even numbers other than 2 are not prime
    # Check for odd factors up to the square root of num
    sqrt_num = int(num ** 0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

# Example usage:
print(is_prime(17))   # Output: True
print(is_prime(15))   # Output: False
