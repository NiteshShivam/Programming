/*
https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
mik-video:
https://youtu.be/V9gXzD7g8fw?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
  */
class Solution
{
	public:
	typedef pair<int,int>P;
	//Function to find sum of weights of edges of the Minimum Spanning Tree.
    int spanningTree(int V, vector<vector<int>> adj[])
    {
        priority_queue<P,vector<P>,greater<P>>pq;
        pq.push({0,0});
        vector<bool> inMST(V,false);
        int sum=0;
        while(!pq.empty()){
            auto p = pq.top();
            pq.pop();
            int weight = p.first;
            int node = p.second;
            if(inMST[node]==true){
                continue;
            }
            inMST[node]=true;
            sum+=weight;
            for(auto &temp:adj[node]){
                int nei = temp[0];
                int we = temp[1];
                pq.push({we,nei});
            }
        }
        return sum;
    }
};
