/*
https://leetcode.com/problems/linked-list-in-binary-tree/
mik-video:
https://youtu.be/Ypzg7G3kg5A
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool solve(TreeNode* root,ListNode* head){
        if(head==NULL){
            return true;
        }
        if(root==NULL){
            return false;
        }
        if(root->val==head->val){
            bool left=solve(root->left,head->next);
            bool right = solve(root->right,head->next);
            return left||right;
        }
        else{
            bool left = solve(root->left,head);
            bool right = solve(root->right,head);
            return left||right;
        }
    }
    bool check(ListNode* head,TreeNode *root){
        if(head==NULL){
            return true;
        }
        if(root==NULL){
            return false;
        }
        
        if(head->val!=root->val){
           return false;
        }
        return check(head->next,root->left)||check(head->next,root->right);
    }
    bool isSubPath(ListNode* head, TreeNode* root) {
        // return solve(root,head);
        if(root==NULL){
            return false;
        }
        return check(head,root)||isSubPath(head,root->left)||isSubPath(head,root->right);
    }
};
