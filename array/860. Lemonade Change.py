'''
https://leetcode.com/problems/lemonade-change/description/
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        current = 0
        five=0
        ten =0
        twenty =0
        for i in range(len(bills)):
            t = bills[i]
            if t==5:
                five+=5
                current = current + 5
            elif t==10:
                if five:
                    five-=5
                    ten+=10
                else:
                    return False
            else:
                if ten and five:
                    ten-=10
                    five-=5
                    twenty+=20
                elif five>=15:
                    five-=15
                    twenty+=20
                else:
                    return False
                
            
        return True
