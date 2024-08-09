'''
https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1
'''
class Solution:
    def countDistinct(self, A, N, K):
        result = []
        space = {}
        for i in range(K):
            temp = A[i]
            space[temp] = space.get(temp,0)+1
        j= K-1
        i =0
        while j<N:
            result.append(len(space))
            temp = A[i]
            space[temp]-=1
            if space[temp]==0:
                del space[temp]
            i+=1
            j+=1
            
            if j<N:
                temp2 = A[j]
                if temp2 not in space:
                    space[temp2]=0
                space[temp2]+=1
        return result
