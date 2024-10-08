/*
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
mik-video
https://youtu.be/W61jIP-O8lw
  */
class Solution {
public:
    int minSwaps(string s) {
        stack<char> st;
        for(int i=0;i<s.size();i++){
            if(st.empty()){
                st.push(s[i]);
            }
            else{
                if(s[i]==']'){
                    if(st.top()=='['){
                        st.pop();
                    }
                    else{
                        st.push(s[i]);
                    }
                }
                else {
                        st.push(s[i]);
                    }
              
            }
        
    }
    int r = st.size()/2;
    return (r+1)/2;
    }
};


// Approach 2

class Solution {
public:
    int minSwaps(string s) {
        int st=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='['){
                st++;
            }
            else if(st>0){
                st--;
            }
        }
         return (st+1)/2;
    }
   
    
};
