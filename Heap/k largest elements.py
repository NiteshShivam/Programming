'''
https://www.geeksforgeeks.org/problems/k-largest-elements4206/1
'''
import heapq

class Solution:

	def kLargest(self,arr, n, k):
		# code here
		hp = []
		for i in range(n):
		    heapq.heappush(hp,arr[i])
		    if len(hp)>k:
		        heapq.heappop(hp)
	    hp.sort(reverse=True)
	    return hp
