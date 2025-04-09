'''
Given an integer x, return true if x is a palindrome , and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


'''

'''
Converting to string method:

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

'''

#optimized version
class Solution(object):
    def isPalindrome(self, x):
        back_half = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        while x > back_half:
            back_half = back_half * 10 + (x % 10)
            x = x // 10
        return x == back_half or x == back_half // 10