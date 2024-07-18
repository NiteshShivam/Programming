'''
You are given an array arr. Your task is to find the longest length of a good sequence. 
A good sequence {x1, x2, .. xn} is an alternating sequence if its elements satisfy one of the following relations :

1.  x1 < x2 > x3 < x4 > x5. . . . . and so on
2.  x1 >x2 < x3 > x4 < x5. . . . . and so on

https://www.youtube.com/watch?v=YrtczUOlRC8
https://www.geeksforgeeks.org/problems/longest-alternating-subsequence5951/1
'''

class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        increasing = 1
        decreasing = 1
        length = len(arr)
        for i in range(1,length):
            if arr[i]>arr[i-1]:
                increasing = max(increasing,decreasing+1)
            elif arr[i]<arr[i-1]:
                decreasing = max(increasing+1,decreasing)
                
        return max(increasing,decreasing)
