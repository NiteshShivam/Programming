'''
https://www.geeksforgeeks.org/problems/burning-tree/1

'''
# python

from collections import deque
class Solution:

    
    def minTime(self, root,target):
        self.map = {}
        self.map[root]=None
        q = deque()
        q.append(root)
        temp = None
        while q:
            node = q.popleft()
            if node.data==target:
                temp=node
            if node.left:
                self.map[node.left]=node
                q.append(node.left)
            if node.right:
                self.map[node.right]=node
                q.append(node.right)
        
        result =0      
        visited = set()
        visited.add(temp)
        q.append(temp)
        while q:
            length = len(q)
            while length:
                node = q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if node in self.map and self.map[node]!=None and self.map[node] not in visited:
                    q.append(self.map[node])
                    visited.add(self.map[node])
                length-=1
            result+=1
        if result>=1:
            return result-1
        return result

# cpp
=====================================

class Solution {
  public:
    int minTime(Node* root, int target) 
    {
        unordered_map<Node*,Node*> parent;
        parent[root]=nullptr;
        queue<Node*> q;
        q.push(root);
        Node* node;
        Node* Target;
        while(!q.empty()){
            node = q.front();
            if(node->data==target){
                Target=node;
            }
            q.pop();
            if(node->left){
                parent[node->left]=node;
                q.push(node->left);
            }
            if(node->right){
                parent[node->right]=node;
                q.push(node->right);
            }
            
        }
        int result=0;
        unordered_set<Node*> visited;
        visited.insert(Target);
        q.push(Target);
        while(!q.empty())
        {
            int length = q.size();
            while(length--){
             node = q.front();
             q.pop();
             if(node->left && visited.find(node->left)==visited.end()){
                 visited.insert(node->left);
                 q.push(node->left);
             }
             if(node->right && visited.find(node->right)==visited.end()){
                 visited.insert(node->right);
                 q.push(node->right);
             }
             if(parent[node] && visited.find(parent[node])==visited.end()){
                 visited.insert(parent[node]);
                 q.push(parent[node]);
             }
            }
            result++;
            
        }
        return result>0 ?result-1:-1;
    }
