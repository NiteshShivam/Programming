'''
https://www.geeksforgeeks.org/problems/partition-a-number-into-two-divisible-parts3605/1
'''
class Solution:
    def stringPartition(ob,S,a,b):
        length = len(S)
        current = ""
        for i in range(length-1):
            current =current+S[i]
            if int(current)%a==0 and int(S[i+1:])%b==0:
                return current+' '+S[i+1:]
        return "-1"
