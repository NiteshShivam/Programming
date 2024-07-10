'''

Topics
Companies
Hint
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.


https://leetcode.com/problems/crawler-log-folder/description/
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        i = 0
        for each in logs:
            if each=='./':
                continue
            elif each=='../':
                if i>0:
                    i-=1
            else:
                i+=1
        return i

Approach 2
from collections import deque
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for each in logs:
            if each=='./':
                continue
            elif each=='../':
                if stack:
                    stack.pop()
            else:
                stack.append(each)
        return len(stack)
        
