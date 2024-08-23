'''
https://leetcode.com/problems/fraction-addition-and-subtraction/description/
https://youtu.be/Uh-KE4D2MOM
'''
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nume = 0
        deno = 1
        length = len(expression)
        i=0
        while i<length:
            currNum =0
            currDeno =  0
            isNeg = True if expression[i]=='-' else False
            if expression[i]=='+' or expression[i]=='-':
                i+=1
            while i<length and expression[i].isdigit():
                val = ord(expression[i])-ord('0')
                currNum = currNum*10+val
                i+=1
            i+=1
            if isNeg:
                currNum *= -1
            while i<length and expression[i].isdigit():
                val = ord(expression[i])-ord('0')
                currDeno = currDeno*10+val
                i+=1
            nume = nume*currDeno + currNum*deno
            deno = deno*currDeno
        gcd = abs(math.gcd(nume,deno))
        nume=nume//gcd
        deno = deno//gcd
        return str(nume)+"/"+str(deno)
