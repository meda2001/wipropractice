def findMaxConsecutiveOnes(nums):
    max_ones = 0
    current_ones = 0
    
    for num in nums:
        if num == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0
    
    return max_ones

# Example usage:
nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))  # Output: 3
