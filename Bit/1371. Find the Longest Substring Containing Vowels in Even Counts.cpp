/*
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
mik-video:
https://youtu.be/6Xf5LfM-ciI
  */
class Solution {
public:
    int findTheLongestSubstring(string s) {
        unordered_map<string,int> mp;
        vector<int> state(5,0);
        string current = "00000";
        int result=0;
        mp[current]=-1;
        for(int i=0;i<s.length();i++){
            if(s[i]=='a'){
                state[0]=(state[0]+1)%2;
            }
            else if(s[i]=='e'){
                state[1]=(state[1]+1)%2;
            }
            else if(s[i]=='i'){
                state[2]=(state[2]+1)%2;
            }
            else if(s[i]=='o'){
                state[3]=(state[3]+1)%2;
            }
            else if(s[i]=='u'){
                state[4]=(state[4]+1)%2;
            }
            current="";
            for(int j =0;j<5;j++){
                current += to_string(state[j]);
            }
            if(mp.find(current)!=mp.end()){
                result = max(result,i-mp[current]);
            }
            else{
                mp[current]=i;
            }
        }
        return result;
    }
};
