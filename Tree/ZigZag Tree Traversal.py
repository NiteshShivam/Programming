'''
https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1
'''
from collections import deque
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        odd =1
        stack1 = deque()
        stack2 = deque()
        stack1.append(root)
        result = []
        while stack1 or stack2:
            if odd:
                length = len(stack1)
                while length:
                    top = stack1.pop()
                    result.append(top.data)
                    
                    if top.left:
                        stack2.append(top.left)
                    if top.right:
                        stack2.append(top.right)
                        
                    length-=1
            else:
                length = len(stack2)
                while length:
                    top = stack2.pop()
                    result.append(top.data)
                    
                    if top.right:
                        stack1.append(top.right)
                    if top.left:
                        stack1.append(top.left)
                    
                        
                    length-=1
            odd = not odd
        return result

# cpp
===================
class Solution{
    public:
    //Function to store the zig zag order traversal of tree in a list.
    vector <int> zigZagTraversal(Node* root)
    {
    	vector<int> result;
    	bool odd = true;
    	deque<Node*> stack1,stack2;
    	stack1.push_back(root);
    	
    	while(!stack1.empty() || !stack2.empty()){
    	    if(odd){
    	        int length = stack1.size();
    	        while(length){
    	            Node* temp = stack1.back();
    	            stack1.pop_back();
    	            result.push_back(temp->data);
    	            if(temp->left){
    	                stack2.push_back(temp->left);
    	                
    	            }
    	            if(temp->right){
    	                stack2.push_back(temp->right);
    	            }
    	            length--;
    	        }
    	        
    	    }
    	    else
    	    {
    	        int length = stack2.size();
    	        while(length){
    	            Node* temp = stack2.back();
    	            stack2.pop_back();
    	            result.push_back(temp->data);
    	            if(temp->right){
    	                stack1.push_back(temp->right);
    	            }
    	            if(temp->left){
    	                stack1.push_back(temp->left);
    	                
    	            }
    	             length--;
    	            
    	        }
    	       
    	        
    	    }
    	    odd = !odd;
    	}
    	return result;
    }
};
