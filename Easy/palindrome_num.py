









class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        b = int(str(x)[::-1])
        if x == b:
            return True
        else:
            return False
