'''
https://www.geeksforgeeks.org/problems/pattern-searching4145/1
'''
class Solution:
	def search(self, text, pat):
	    i = 0
	    start=0
	    j = 0
	    while i<len(text) and j<len(pat):
	        if text[i]==pat[j]:
	            if j==0:
	                start=i
	                
	            i+=1
	            j+=1
	            
	        elif j!=0:
	            i=start+1
	            j=0
	        else:
	            i+=1
	       # if j==len(pat):
	       #    return 1
	        
        if j==len(pat):
            return 1
	    return 0
