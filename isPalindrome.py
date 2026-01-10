# 125. Valid Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consis


# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# txt = "CompanyX"
# x = txt.isalpha()
# print(x) --> True


# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
# txt = "Company12"
# x = txt.isalnum()
# print(x) --> True



def isPalindrome(self, s: str) -> bool:
    # Step 1: Convert the string to lowercase
    # This ensures case-insensitive comparison (A == a)
    s = s.lower()

    # Step 2: Create an empty string to store only alphanumeric characters
    result = ""

    # Step 3: Remove all non-alphanumeric characters
    # Keep only letters and digits
    for ch in s:
        if ch.isalnum():
            result += ch

    # Step 4: Initialize two pointers
    # i starts from the beginning
    # j starts from the end
    i = 0
    j = len(result) - 1

    # Step 5: Compare characters from both ends
    while i <= j:
        # If characters do not match, it is not a palindrome
        if result[i] != result[j]:
            return False

        # Move pointers inward
        i += 1
        j -= 1

    # Step 6: If all characters match, it is a palindrome
    return True
# s = "A man, a plan, a canal: Panama"

