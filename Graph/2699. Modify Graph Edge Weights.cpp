/*
https://leetcode.com/problems/modify-graph-edge-weights/description/

mik-video:
https://youtu.be/F6sRIQKslwA
  */
class Solution {
public:
    typedef long long ll;
    const int large_value =2e9;
    typedef pair<long,long>P;
    ll Dijsktra( vector<vector<int>>& edges,int source,int destination,int n){
        vector<ll> result(n,INT_MAX);
        unordered_map<ll,vector<pair<ll,ll>>> adj;
        for(vector<int>&edge:edges){
            if(edge[2]!=-1){
                int u = edge[0];
                int v = edge[1];
                int wt = edge[2];
                adj[u].push_back({v,wt});
                adj[v].push_back({u,wt});
            }
        }
        result[source]=0;
        priority_queue<P,vector<P>,greater<P>>pq;
        pq.push({0,source});
        while(!pq.empty()){
            ll currDist = pq.top().first;
            ll currNode = pq.top().second;
            pq.pop();
            for(auto &[nbr,wt]:adj[currNode]){
                if(wt+currDist<result[nbr]){
                    result[nbr]=wt+currDist;
                    pq.push({result[nbr],nbr});
                }
            }
        }
        return result[destination];
    }
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        ll currShortestDist = Dijsktra(edges,source,destination,n);
        if(currShortestDist<target){
            return {};
        }

        bool match = currShortestDist==target;
        if(match==true){
            for(vector<int>& edge:edges){
                if(edge[2]==-1){
                    edge[2]=large_value;
                }
            }
        }
        for(vector<int>&edge:edges){
            if(edge[2]==-1){
                edge[2]=(match==true)?large_value:1;
                if(match!=true){
                    ll newShortestDist = Dijsktra(edges,source,destination,n);
                    if(newShortestDist<=target){
                        edge[2]+=target-newShortestDist;
                        match=true;
                    }
                }
            }
        }
        if(match==false){
            return {};
        }
        return edges;
    }
};

// python 
// time limit exceed
=============================================

 class Solution:
    def Dijkstra(self,edges,n,source,destination):
        adj = defaultdict(list)
        for each in edges:
            u = each[0]
            v = each[1]
            w = each[2]
            if w!=-1:
                adj[u].append((w,v))
                adj[v].append((w,u))
        result = [float('inf')]*n
        result[source]=0
        pq = [(0,source)]
        while pq:
            cDist,cNode = heapq.heappop(pq)
            for each in adj[cNode]:
                if each[0]+cDist<result[each[1]]:
                    result[each[1]]=each[0]+cDist
                    heapq.heappush(pq,(result[each[1]],each[1]))
                    
        return result[destination]


    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        large_value = 2e9
        currDist = self.Dijkstra(edges,n,source,destination)
        if currDist<target:
            return []
        match=False
        if currDist==target:
            match=True
        for each in edges:
            if each[2]==-1:
                each[2] = large_value if match else 1
            if not match:
                newShort = self.Dijkstra(edges,n,source,destination)
                if newShort<=target:
                    each[2]+=target-newShort
                    match=True
        if not match:
            return []
        return edges
