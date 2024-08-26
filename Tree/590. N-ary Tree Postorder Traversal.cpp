// https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> result;
    void solve(Node* root){
        if(root==NULL){
            return;
        }
        for(const auto& each:root->children){
            solve(each);
        }
        result.push_back(root->val);
    }
    vector<int> postorder(Node* root) {
        solve(root);
        return result;
    }
};

===================================


  """
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

  
class Solution:
    def solve(self,root):
        if not root:
            return
        for each in root.children:
            self.solve(each)
        self.result.append(root.val)
    def postorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.solve(root)
        return self.result
