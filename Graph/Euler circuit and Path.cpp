/*
https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1

mik-video:
part-1
https://youtu.be/CeO0JEX4QAc?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
part -2
https://youtu.be/i8h_O6u3DSc?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
  */
class Solution {
public:
    void dfs(vector<bool>& visited,int u,vector<int>adj[]){
        visited[u]=true;
        for(auto it:adj[u]){
            if(visited[it]==false){
                dfs(visited,it,adj);
            }
            
        }
    }
    bool isConnected(int V,vector<int>adj[]){
        int nonZerovertex  =-1;
        for(int i=0;i<V;i++){
            if(adj[i].size()>0){
                nonZerovertex =i;
                break;
            }
        }
        vector<bool> visited(V,false);
        dfs(visited,nonZerovertex,adj);
        for(int i=0;i<V;i++){
            if(visited[i]==false && adj[i].size()>0){
                return false;
            }
        }
        return true;
        
    }
	int isEulerCircuit(int V, vector<int>adj[]){
	   if(isConnected(V,adj)==false){
	     return 0;
	   }
	   int count=0;
	   for(int i=0;i<V;i++){
	        if(adj[i].size()%2==1){
	            count+=1;
	        }
	   }
	   if(count>2){
	       return 0;
	   }
	   else if(count==2){
	       return 1;
	   }
	   return 2;
	}
};
