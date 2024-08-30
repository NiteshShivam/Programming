'''
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
mik-video
https://youtu.be/JS48Hp2_Z4I?list=PLpIkg8OmuX-I99uuP2BZOz4mI_lms4gVG

'''
# cpp
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
class Solution:
    def insert(self,root,num):
        temp = root
        for i in range(31,-1,-1):
            i_bth = (num>>i)&1
            if i_bth==0:
                if temp.left==None:
                    temp.left = TrieNode()
                temp =temp.left
            else:
                if temp.right==None:
                    temp.right = TrieNode()
                temp=temp.right
    def find(self,root,num):
        temp =root
        maxXor = 0
        for i in range(31,-1,-1):
            i_bth = (num>>i)&1
            if (i_bth==0):
                if temp.right:
                    maxXor += pow(2,i)*1
                    temp = temp.right
                else:
                    maxXor += pow(2,i)*0
                    temp = temp.left
            else:
                if temp.left:
                    maxXor += pow(2,i)*1
                    temp = temp.left
                else:
                    maxXor += pow(2,i)*0
                    temp = temp.right
        return maxXor
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            self.insert(root,num)
        result = 0
        for num in nums:

            xorResult =self.find(root,num)
            result = max(xorResult,result)
        return result




=================================================================

class Solution {
public:
    struct trieNode{
        trieNode* left;
        trieNode* right;
    };
    void insert(trieNode* root,int &num){

        trieNode* temp = root;
        for(int i=31;i>=0;i--){
            int i_bit = (num>>i)&1;
            if(i_bit==0){
                if(temp->left==NULL){
                    temp->left=new trieNode();
                }
                temp=temp->left;
            }
            else{
                if(temp->right==NULL){
                    temp->right=new trieNode();
                }
                temp = temp->right;
            }
        }
    }
    int findMax(trieNode* root,int &num){
        trieNode* temp = root;
        int maxXor = 0;
        for(int i=31;i>=0;i--){
            int i_bit = (num>>i)&1;
            if(i_bit==0){
                if(temp->right!=NULL){
                    maxXor += pow(2,i)*1;
                    temp=temp->right;
                }
                else{
                    maxXor += pow(2,i)*0;
                    temp=temp->left;
                }

            }
            else{
                if(temp->left!=NULL){
                    maxXor+=pow(2,i)*1;
                    temp=temp->left;
                }
                else{
                    maxXor +=pow(2,i)*0;
                    temp=temp->right;
                }
            }
        }
        return maxXor;
    }
    int findMaximumXOR(vector<int>& nums) {
        trieNode* root = new trieNode();
        for(int &num:nums){
            insert(root,num);
        }
        int result = 0;

        for(int i=0;i<nums.size();i++){
            int temp = findMax(root,nums[i]);
            result = max(result,temp);
        }

        return result;
    }
};
