'''Given an array arr of positive integers and another number x. 
Determine whether or not two elements exist in arr whose sum is exactly x.
'''
#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		hashMap = set()
		for each in arr:
		    required = x-each
		    if required in hashMap:
		        return True
		    hashMap.add(each)
		return False
