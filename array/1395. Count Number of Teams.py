'''

https://leetcode.com/problems/count-number-of-teams/description/
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        increasing = 0
        desreasing = 0
        result =0
        length = len(rating)
        for i in range(length):
            leftSmall=0
            leftGreater = 0
            rightSmall = 0
            rightGreater=0
            for l in range(0,i):
                value = rating[l]
                if value<rating[i]:
                    leftSmall+=1
                if value>rating[i]:
                    leftGreater +=1
            for r in range(i+1,length):
                value =rating[r]
                if value<rating[i]:
                    rightSmall+=1
                if value>rating[i]:
                    rightGreater+=1
            increasing += leftSmall*rightGreater
            desreasing += leftGreater*rightSmall
        return increasing+desreasing
