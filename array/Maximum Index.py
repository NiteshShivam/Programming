'''
https://www.geeksforgeeks.org/problems/maximum-index3307/1
https://discuss.geeksforgeeks.org/comment/69eb6f4925dac4045e3d935b5e8ca51f/practice
'''
#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		
		v_min = [arr[0]]
		v_max = [0]*n
		v_max[-1] = arr[-1]
		for i in range(1,n):
		    v_min.append(min(arr[i],v_min[i-1]))
		    v_max[n-i-1] = max(arr[n-i-1],v_max[n-i])
		ans = 0
		i =0
		j=0
		while i<n and j<n:
		    if v_min[i]<=v_max[j]:
		        ans = max(ans,j-i)
		        j+=1
		    else:
		        i+=1
		return ans
