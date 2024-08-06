'''
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
'''
class Solution:
    def minimumPushes(self, word: str) -> int:
        space = {}
        one = 0
        two = 0
        three=0
        four = 0
        cost = 0
        space2 = {}
        for each in word:
            if each not in space2:
                space2[each]=0
            space2[each]+=1
        letter = sorted(space2,key=lambda x:-space2[x])
        
        for each in letter:
            if one<8:
                one+=1
                cost = cost + space2[each]*1
            elif two<8:
                cost = cost + space2[each]*2
                two+=1
            elif three<8:
                cost = cost + space2[each]*3
                three+=1
            else:
                cost = cost + space2[each]*4
            
        return cost
        
