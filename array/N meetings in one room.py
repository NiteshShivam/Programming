'''
There is one meeting room in a firm. There are n meetings in the form of (start[i], end[i]) where start[i] 
is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting 
room when only one meeting can be held in the meeting room at a particular time?
Return the maximum number of meetings that can be held in the meeting room.


https://www.youtube.com/watch?v=mKfhTotEguk
https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
'''
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meet = []
        for i in range(n):
            meet.append((start[i],end[i]))
        meet.sort(key = lambda x:x[1])
        result = 0
        last = 0
        for each in meet:
            u = each[0]
            v = each[1]
            if last<u:
                last = v
                result+=1
        return result
