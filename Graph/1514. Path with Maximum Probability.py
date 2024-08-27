'''
https://leetcode.com/problems/path-with-maximum-probability/description/
https://youtu.be/zTM9k6jqpXI
'''
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        result = [float('-inf')]*n
        pq = []
        adj = defaultdict(list)
        i=0
        for each in edges:
            adj[each[0]].append([each[1],succProb[i]])
            adj[each[1]].append([each[0],succProb[i]])
            i+=1
        result[start_node]=1
        heapq.heappush(pq,(-1,start_node))
        while pq:
            value,node = heapq.heappop(pq)
            for each in adj[node]:
                new_node = each[0]
                prob = -(each[1])
                if value*prob>result[new_node]:
                    result[new_node] = value*prob
                    heapq.heappush(pq,(-result[new_node],new_node))
        # print(result)
        if result[end_node]==float('-inf'):
            return  0.00000
        return result[end_node]


# cpp
======================================
class Solution {
public:
    typedef pair<double,int>p;
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        unordered_map<int,vector<pair<int,double>>> adj;
        vector<double> result(n,0);
        for(int i=0;i<edges.size();i++)
        {
            adj[edges[i][0]].push_back({edges[i][1],succProb[i]});
            adj[edges[i][1]].push_back({edges[i][0],succProb[i]});
        }
        priority_queue<p> pq;
        
        result[start_node]=1.0;
        pq.push({1.0,start_node});
        while(!pq.empty()){
            int currentNode = pq.top().second;
            double prob = pq.top().first;
            pq.pop();
            for(auto &temp:adj[currentNode]){
                double adjProb = temp.second;
                int adjNode = temp.first;
                if(result[adjNode]<adjProb*prob){
                    result[adjNode]=adjProb*prob;
                    pq.push({result[adjNode],adjNode});
                }
            }

        }
        if(result[end_node]==0){
            return 0.0;
        }
        return result[end_node];
    }
};
