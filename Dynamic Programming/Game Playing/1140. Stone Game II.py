'''
https://leetcode.com/problems/stone-game-ii/description/

https://youtu.be/9f1vzDFVnGA
'''
class Solution:
    def solveAlice(self,person,index,m):
        if index>=self.length:
            return 0
        result = -1 if person==1 else float('inf')
        stones = 0
        if (person,index,m) in self.memo:
            return self.memo[(person,index,m)]
        for x in range(1,min(2*m,self.length-index)+1):
            stones +=self.piles[index+x-1]
            if person==1:
                result = max(result,stones+self.solveAlice(0,index+x,max(m,x)))
            else:
                result = min(result,self.solveAlice(1,index+x,max(m,x)))
        self.memo[(person,index,m)] = result
        return result

    def stoneGameII(self, piles: List[int]) -> int:
        self.length =  len(piles)
        self.piles = piles
        self.memo = {}
        # person 1 Alice ,index ,starting value of M
        return self.solveAlice(1,0,1)
