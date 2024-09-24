/*
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
mik-video:

https://youtu.be/OZNS72LANFU
  */
struct TrieNode{
    TrieNode* children[10];
};
class Solution {
public:
    TrieNode* getTrieNode(){
        TrieNode* node = new TrieNode();
        for(int i=0;i<10;i++){
            node->children[i]=nullptr;
        }
        return node;
    }
    void insert(int num,TrieNode* root){
        TrieNode* crawl =root;
        string n = to_string(num);
        for(char ch:n){
            int idx = ch-'0';
            if(crawl->children[idx]==nullptr){
                crawl->children[idx]=getTrieNode();
            }
            crawl=crawl->children[idx];
        }
    }
    int  search(int num,TrieNode* root){
        TrieNode* crawl = root;
        string n = to_string(num);
        int length=0;
        for(char ch:n){
            int idx = ch-'0';
            if(crawl->children[idx]!=nullptr){
                length+=1;
                crawl = crawl->children[idx];
            }
            else{
                break;
            }
        }
        return length;
    }

    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        TrieNode* root = getTrieNode();
        for(int num:arr1){
            insert(num,root);
        }
        int result = 0;
        for(int num : arr2){
            result = max(result,search(num,root));
        }
        return result;
    }
};


===========================================================

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        int result = 0;
        unordered_set <string> st;
        for(int i=0;i<arr1.size();i++){
           string s1 = to_string(arr1[i]);
           int j=0;
           int l = s1.size();
           while(j<l){
            st.insert(s1.substr(0,j+1));
            j+=1;
           }
        }
        for(int i=0;i<arr2.size();i++){
            string s1 = to_string(arr2[i]);
            int j=0;
            int l=s1.size();
            while(j<l){
                if(st.find(s1.substr(0,j+1))!=st.end()){
                    result = max(result,j+1);
                }
                else{
                    break;
                }
                j+=1;
            }
        }
        return result;
    }
};
