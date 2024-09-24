/*
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
mik-video:

https://youtu.be/OZNS72LANFU
  */


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
