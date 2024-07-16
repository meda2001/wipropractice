def lengthOfLongestSubstring(s):
    seen = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in seen and start <= seen[char]:
            start = seen[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        seen[char] = end
    
    return max_length

# Example usage:
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3
