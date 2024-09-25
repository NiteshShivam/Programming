/*
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
mik-video:
https://youtu.be/PRHedN3h2Gc
  */
struct TrieNode{
        TrieNode *children[26];
        int count=0;
    };
class Solution {
public:
    TrieNode* getNode(){
        TrieNode *node = new TrieNode();
        for(int i=0;i<26;i++){
            node->children[i]=nullptr;
        }
        // node->count=0;
        return node;
    }
    void insert(string &s,TrieNode *root){
        TrieNode *crawl =root;
        for(char ch:s){
            int idx = ch-'a';
            if(crawl->children[idx]==nullptr){
                crawl->children[idx]=getNode();
            }
            crawl=crawl->children[idx];
            crawl->count+=1;
        }
    }
    int getScore(string &s,TrieNode* root){
        int r=0;
        TrieNode *crawl = root;
        for(char ch:s){
            int idx = ch-'a';
            if(crawl->children[idx]!=nullptr){
                crawl = crawl->children[idx];
                r += crawl->count;
            }
            else{
                break;
            }
        }
        return r;
    }

    vector<int> sumPrefixScores(vector<string>& words) {
        int n = words.size();
        TrieNode *root = getNode();
        for(int i=0;i<n;i++){
            insert(words[i],root);
        }
        vector<int> result(n);
        for(int i=0;i<n;i++){
            result[i] = getScore(words[i],root);
        }
        return result;
        
    }
};
