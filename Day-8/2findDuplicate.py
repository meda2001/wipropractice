def findDuplicate(nums):
    slow = nums[0]
    fast = nums[nums[0]]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
