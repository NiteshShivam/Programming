'''
https://leetcode.com/problems/spiral-matrix-iii/description/
https://youtu.be/dt0UzAz7SPg
'''
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        steps = 0
        dire = 0
        result = [[rStart,cStart]]
        while len(result)<rows*cols:
            if dire==0 or dire==2:
                steps+=1
            for i in range(steps):
                rStart += direction[dire][0]
                cStart += direction[dire][1]
                if rStart>=0 and rStart<rows and cStart>=0 and cStart<cols:
                    result.append([rStart,cStart])
            dire = (dire +1)%4
        return result
