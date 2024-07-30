'''
https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
'''
class Solution:

	def count(self,arr, n, x):
		# code here
		first = -1
		last = -1
		left = 0
		right = n-1
		while left<=right:
		    mid = left+(right-left)//2
		    if arr[mid]==x:
		        first = mid
		        right = mid-1
		    elif arr[mid]<x:
		        left = mid+1
		    else:
		        right = mid-1
		left = 0
		right = n-1
		while left<=right:
		    mid = left+(right-left)//2
		    if arr[mid]==x:
		        last = mid
		        left = mid+1
		    elif arr[mid]<x:
		        left = mid+1
		    else:
		        right = mid-1
		if first==-1 or last==-1:
		    return 0
		
		return last-first+1
