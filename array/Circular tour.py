'''

https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1
https://youtu.be/tcOcmNHFTTM
'''
class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        
        count = 0
        result=0
        i=-1
        pet = 0
        dis = 0
        for i in range(len(lis)):
            pet +=lis[i][0]
            dis +=lis[i][1]
        if dis>pet:
            return -1
        while count<n:
            i = i+1
            i = i%n
            result =result+lis[i][0]-lis[i][1]
            count+=1
            if result<0:
                count=0
                result=0
        return (i+1)%n








Brute Force (not passing all solution->below)
============================================
class Solution:
    def tour(self,lis, n):
        for i in range(n):
            if lis[i][0]<lis[i][1]:
                continue
            j = (i+1)%n
            currentGas = lis[i][0]-lis[i][1]+lis[j][0]
            while j!=i:
                if currentGas>=lis[j][1]:
                    currentGas -=lis[j][1]
                    j = (j+1)%n
                    currentGas = currentGas+lis[j][0]
                else:
                    break
            if j==i:
                return i
        return -1
