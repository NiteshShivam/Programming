'''
There are n friends that are playing a game. 
The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, 
and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. 
The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle,
go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

 https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

 https://youtu.be/lq3RMxKST-Y

'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        qu = deque()
        for i in range(1,n+1):
            qu.append(i)
        tempK = k-1
        while len(qu)!=1:
            while tempK:
                value = qu.popleft()
                qu.append(value)
                tempK-=1
            qu.popleft()
            tempK=k-1
        return qu.popleft()
