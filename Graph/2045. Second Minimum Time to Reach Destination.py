'''

https://youtu.be/_rnQKrA9xzA
https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/
'''
from collections import deque,defaultdict
class Solution:
    def dijkstra(self,source,adj,V,time,change):
        maxV = float('inf')
        distance1 = [maxV]*(V+1)
        distance2 = [maxV]*(V+1)
        distance1[source]=0
        hp = []
        heapq.heappush(hp,(0,source))
        while hp:
            temp = heapq.heappop(hp)
            samay = temp[0]
            source =temp[1]
            if source==V and distance2[V]!=maxV:
                return distance2[V]
            if (samay//change)%2==1:
                samay = ((samay//change)+1)*change
            for each in adj[source]:
                if samay+time<distance1[each]:
                    distance2[each]=distance1[each]
                    distance1[each]=time+samay
                    heapq.heappush(hp,(time+samay,each))
                elif samay+time<distance2[each] and distance1[each]!=time+samay:
                    distance2[each]=samay+time
                    heapq.heappush(hp,(time+samay,each))
        return -1
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for each in edges:
            u = each[0]
            v = each[1]
            adj[u].append(v)
            adj[v].append(u)
        return  self.dijkstra(1,adj,n,time,change)



# ================================================================================bfS APPROACH 2==
from collections import deque,defaultdict
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for each in edges:
            u = each[0]
            v = each[1]
            adj[u].append(v)
            adj[v].append(u)
        
        maxV = float('inf')
        distance1 = [maxV]*(n+1)
        distance2 = [maxV]*(n+1)
        distance1[1]=0
        queue = deque()
        queue.append((1,1)) # node and its frequency
        while queue:
            node,freq = queue.popleft()
            timePassed = distance1[node] if freq==1 else distance2[node]
            if node==n and distance2[node]!=maxV:
                return distance2[node]
            if (timePassed//change)%2:
                timePassed = ((timePassed//change)+1)*change
            for neigh in adj[node]:
                if distance1[neigh]==maxV:
                    distance1[neigh]=timePassed+time
                    queue.append((neigh,1))
                elif distance2[neigh]==maxV and distance1[neigh]!=timePassed+time:
                    distance2[neigh]=timePassed+time
                    queue.append((neigh,2))
            
        return -1
