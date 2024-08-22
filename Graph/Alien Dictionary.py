'''
https://www.geeksforgeeks.org/problems/alien-dictionary/1
https://youtu.be/U3N_je7tWAs
'''
from typing import List
from collections import defaultdict,deque
class Solution:

    def toposort(self,adj,k):
        result = ""
        indegree = [0]*k
        for i in range(k):
            current_char = chr(97+i)
            
            if current_char in adj:
                for v in adj[current_char]:
                    index = ord(v)-97
                    
                    indegree[index]+=1
        # print(indegree)
        q = deque()
        for i in range(k):
            if indegree[i]==0:
                q.append(i)
        while q:
            current_value = q.popleft()
            current_char = chr(current_value+97)
            result+=current_char
            if current_char in adj:
                for each in adj[current_char]:
                    index = ord(each)-97
                    indegree[index]-=1
                    if indegree[index]==0:
                        q.append(index)
                        
        # print(result)
        return result
        
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        length = len(alien_dict)
        adj = defaultdict(list)
        for i in range(length-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            mlen = min(len(s1),len(s2))
            for j in range(mlen):
                if s1[j]!=s2[j]:
                    adj[s1[j]].append(s2[j])
                    break
        # print(adj)
        return self.toposort(adj,k)
        
        
