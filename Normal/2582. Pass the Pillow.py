'''
There are n people standing in a line labeled from 1 to n. 
The first person in the line is holding a pillow initially. 
Every second, the person holding the pillow passes it to the next person standing in the line. 
Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

 https://leetcode.com/problems/pass-the-pillow/description/
'''
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current = 1
        direction=True
        while time>0:
            if current==n:
                direction = False
            elif current==1:
                direction=True
            if direction==True:
                current=current+1
            elif direction==False:
                current=current-1
            time =time-1
        return current
