/*
https://leetcode.com/problems/longest-common-suffix-queries/description/
mik-video:
https://youtu.be/jZX2Z5DKR2M?list=PLpIkg8OmuX-I99uuP2BZOz4mI_lms4gVG
  */
class Solution {
public:
    struct trieNode{
        int idx;
        trieNode *children[26];
    };
    trieNode* getNode(int i){
        trieNode* temp = new trieNode();
        temp->idx =i;
        for(int j=0;j<26;j++){
            temp->children[j]=NULL;
        }
        return temp;
    }
    void insert(trieNode* root,vector<string>& wordsContainer,int i){
        string word = wordsContainer[i];
        int n = word.length();
        
        for(int j = n-1;j>=0;j--){
            char ch = word[j];
            int ch_idx = ch-'a';
            if(root->children[ch_idx]==NULL){
                root->children[ch_idx] = getNode(i);
            }
            root=root->children[ch_idx];
            if(wordsContainer[root->idx].length()>n){
                root->idx=i;
            }
        }
    }
    int search(trieNode* root,string &word){
        int result_idx = root->idx;
        int n = word.length();
        for(int i=n-1;i>=0;i--){
            int ch = word[i]-'a';
            root = root->children[ch];
            if(root==NULL){
                return result_idx;
            }
            result_idx = root->idx;
        }
        return result_idx;  
    }
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        int m = wordsContainer.size();
        int n = wordsQuery.size();
        vector<int> result(n);
        trieNode* root = getNode(0);
        for(int i=0;i<m;i++){
            int idx = root->idx;
            if(wordsContainer[idx].length()>wordsContainer[i].length()){
                root->idx=i;
            }
             insert(root,wordsContainer,i);
        }
        for(int j=0;j<n;j++){
            result[j] = search(root,wordsQuery[j]);
        }
        return result; 
    }
};



// python
============================================

 class Trie:
    def __init__(self,idx):
        self.idx = idx
        self.children = [None]*26

class Solution:
    def getNode(self,i):
        return Trie(i)
    def insert(self,root,i,wordsContainer):
        word = wordsContainer[i]
        n = len(word)
        for j in range(n-1,-1,-1):
            ch_idx = ord(word[j])-ord('a')
            if root.children[ch_idx] is None:
                root.children[ch_idx]=self.getNode(i)
            root = root.children[ch_idx]
            if len(wordsContainer[root.idx])>n:
                root.idx=i
    def search(self,root,word):
        result_idx = root.idx
        n = len(word)
        for i in range(n-1,-1,-1):
            ch_idx = ord(word[i]) - ord('a')
            root = root.children[ch_idx]
            if root is None:
                return result_idx
            result_idx = root.idx

        return result_idx
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = Trie(0)

       
        m = len(wordsContainer)
        n = len(wordsQuery)
        result = [0]*n
        for i in range(m):
            if(len(wordsContainer[i])<len(wordsContainer[root.idx])):
                root.idx = i
            self.insert(root,i,wordsContainer)
        for i in range(n):
            result[i] = self.search(root,wordsQuery[i])
        return result
