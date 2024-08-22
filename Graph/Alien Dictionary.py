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


# cpp
=================================
class Solution{
    public:
    string toposort(unordered_map<char,vector<char>>& adj,int k){
        string result="";
        vector<int> indegree(k,0);
        for(int i=0;i<k;i++){
            char current_char = 'a'+i;
            if (adj.find(current_char)!=adj.end()){
                for(char v:adj[current_char]){
                    indegree[v-'a']++;
                }
            }
        }
        queue<int> q;
        for(int i=0;i<k;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            int current_value = q.front();
            q.pop();
            char current_char = current_value+'a';
            result.push_back(current_char);
            if (adj.find(current_char)!=adj.end()){
                for(char v:adj[current_char]){
                    indegree[v-'a']--;
                    if(indegree[v-'a']==0){
                        q.push(v-'a');
                    }
                }
            }
        }
        return result;
    }
    string findOrder(string dict[], int N, int K) {
        unordered_map<char,vector<char>> adj;
        for(int i=0;i<N-1;i++){
            string s1 = dict[i];
            string s2 = dict[i+1];
            int mlen=min(s1.size(),s2.size());
            for(int j=0;j<mlen;j++){
                if(s1[j]!=s2[j]){
                    adj[s1[j]].push_back(s2[j]);
                    break;
                }
            }
        }
        return toposort(adj,K);
    }
};
        
