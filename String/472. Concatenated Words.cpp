/*
https://leetcode.com/problems/concatenated-words/description/
mik-video:
https://youtu.be/zZsnMAgM6Q0?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */
class Solution {
public:
    unordered_map<string,bool> dp;
    bool isContcatinat(string &w,unordered_set<string>& st){
        int n = w.length();
        if(dp.find(w)!=dp.end()){
            return dp[w];
        }
        for(int i=0;i<n;i++){
            string prefix = w.substr(0,i+1);
            string suffix = w.substr(i+1);
            if(st.find(prefix)!=st.end() &&(st.find(suffix)!=st.end()|| isContcatinat(suffix,st))){
                return dp[w]=true;
                
            }
        }
        
        return dp[w]= false;
    }
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        vector<string> result;
        dp.clear();
        unordered_set<string>  st(begin(words),end(words));
        int n = words.size();
        for(int i=0;i<n;i++){
            string w = words[i];
            if(isContcatinat(w,st)){
                result.push_back(w);
            }
        }
        return result;
    }
};
