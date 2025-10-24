# Problem: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Date: Oct 25, 2025

class Solution:
    def romanToInt(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev = 0

        for char in reversed(s):
            value = roman_dict[char]
            if value < prev :
                total -= value
            else :
                total += value
            prev = value
        return total
