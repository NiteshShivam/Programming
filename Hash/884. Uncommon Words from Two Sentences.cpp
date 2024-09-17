/*
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

  */
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string,int> mp;
        int n = s1.length();
        string current = "";
        for(int i=0;i<n;i++){
            if(s1[i]==' '){
                mp[current]+=1;
                current ="";
            }
            else{
                current = current+s1[i];
            }
        }
        if(current.length()>=1){
            mp[current]+=1;

        }
        current="";
         n = s2.length();
        for(int i=0;i<n;i++){
            if(s2[i]==' '){
                mp[current]+=1;
                current ="";
            }
            else{
                current = current+s2[i];
            }
        }
        if(current.length()>=1){
            mp[current]+=1;
        }
        vector<string>result;
        for(auto t:mp){
            if(t.second==1){
                result.push_back(t.first);
            }
        }
        return result;
    }
};
