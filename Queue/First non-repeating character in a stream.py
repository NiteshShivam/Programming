'''

https://youtu.be/_gJ3to4RyeQ?t=2388
https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1
'''
from collections import deque
class Solution:
	def FirstNonRepeating(self, A):
		charCount = [0]*26
		q = deque()
		length = len(A)
		result = ""
		for i in range(length):
		    char = A[i]
		    index  = ord(char)-ord('a')
		    charCount[index]+=1
		    q.append(char)
		    while q:
		        ch = q[0]
		        index  = ord(ch)-ord('a')
		        if charCount[index]>1:
		            q.popleft()
		        else:
		            result = result+ch
		            break
		    if not q:
		        result+='#'
        return result
