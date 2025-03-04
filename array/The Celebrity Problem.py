'''
https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
'''

'''A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people,
find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j 
is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Return the index of the celebrity, if there is no celebrity return -1.
Note: Follow 0 based indexing.
Follow Up: Can you optimize it to O(N)

'''
Approach :
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        
        result = [0]*n
        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    result[i]+=1
        total = 0
        aamirKhan = -1
        for i in range(n):
            if result[i]==0:
                total+=1
                aamirKhan = i
        if total==1:
            for i in range(n):
                if i!=aamirKhan and M[i][aamirKhan]!=1:
                    return -1
            return aamirKhan
                    
        return -1
            
                
                
Approach 2:

#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        result = -1
        count =0
        for i in range(n):
            if M[i].count(1)==0:
                result = i
                count+=1
        #print(count)
        if count==1:
            for i in range(n):
                if i!=result and M[i][result]!=1:
                    return -1
            return result
        return -1

Approach 3: using stack

#User function Template for python3
from collections import deque
class Solution:
    
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        stack = deque()
        for i in range(n):
            stack.append(i)
        while len(stack)>1:
            first = stack.pop()
            second = stack.pop()
            if M[first][second]==1 and M[second][first]==0:
                stack.append(second)
            elif M[second][first]==1 and M[first][second]==0:
                stack.append(first)
        if not stack:
            return -1
        aamir = stack.pop()
        #print(aamir)
        for i in range(n):
            if i!=aamir and M[i][aamir]!=1:
                return -1
            if M[aamir][i]==1:
                return -1
        return aamir
