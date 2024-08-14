'''
https://www.geeksforgeeks.org/problems/implement-strstr/1
'''
def strstr(s,x):
    #code here
    n = len(s)
    m = len(x)
    if m>n:
        return -1
    def match(i,j):
        t = i
        while i<n and  j<m:
            if s[i]!=x[j]:
                return -1
            i+=1
            j+=1
        if j!=m:
            return -1
        return t
    for i in range(n):
        if s[i]==x[0]:
            ans = match(i,0)
            if ans!=-1:
                return ans
    return -1
