'''
https://www.geeksforgeeks.org/problems/palindrome0746/1
'''
class Solution:
	def is_palindrome(self, n):
		x = 0
		t = n
		while t>0:
		    x = x*10 + t%10
		    t = t//10
		while x>0:
		    if x%10!=n%10:
		        return "No"
		    x = x//10
		    n = n//10
	    return "Yes"
