# Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Date: Oct 23, 2025

class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        b = int(str(x)[::-1])
        if x == b:
            return True
        else:
            return False
