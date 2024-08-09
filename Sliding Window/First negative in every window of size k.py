'''
https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
'''
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    result = []
    temp = 0
    q = deque()
    for i in range(K):
        if A[i]<0:
            q.append(A[i])
    i = 0
    j = K-1
    while j<N:
        if len(q):
            result.append(q[0])
        else:
            result.append(0)
        temp1 = A[i]
        if q and q[0]==temp1:
            q.popleft()
        i+=1
        j+=1
        if j<N:
            temp2 = A[j]
            if temp2<0:
                q.append(temp2)
    return result
