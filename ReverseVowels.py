# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.




#============================================ Solution 
# Given string
s = "IceCreAm"

# Convert string to list because strings are immutable in Python
s = list(s)

# Initialize two pointers
# i -> starts from the beginning
# j -> starts from the end
i = 0
j = len(s) - 1

# Set of vowels (both lowercase and uppercase)
# Using set for O(1) lookup time
vowels = set('aeiouAEIOU')

# Loop until the two pointers cross
while i < j:

    # If left pointer is not a vowel,
    # move it forward
    if s[i] not in vowels:
        i += 1

    # If right pointer is not a vowel,
    # move it backward
    elif s[j] not in vowels:
        j -= 1

    # If both characters are vowels,
    # swap them and move both pointers
    else:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

# Convert list back to string
s = "".join(s)

# Print the final result
print(s)






