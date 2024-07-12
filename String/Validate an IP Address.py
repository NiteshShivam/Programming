'''
Write a program to Validate an IPv4 Address.
According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, 
each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1 .
A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255.
Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255).
Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Your task is to complete the function isValid which returns 1 if the given IPv4 address is valid else returns 0.
The function takes the IPv4 address as the only argument in the form of string.





https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1
'''

def isValid(s):
    dot = 0
    
    number = ('0','1','2','3','4','5','6','7','8','9')
    length = len(s)
    if length<7 or length>15:
        return False
    for c in s:
        if c=='.':
            dot+=1
        elif c not in number:
            return False
    if dot!=3:
        return False
    
    temp=""
    for i in range(length):
        if s[i]!='.':
            temp+=s[i]
        else:
            if len(temp)>1 and temp[0]=='0':
                return False
            if 0<=int(temp)<=255:
                temp=""
            else:
                return False
    if len(temp)>1 and temp[0]=='0':
        return False
    if 0<=int(temp)<=255:
        return True
    return False
