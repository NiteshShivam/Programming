/*
https://leetcode.com/problems/make-the-string-great/description/
mik-video:
https://youtu.be/J43ZIltH3AY?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */

class Solution {
public:
    string makeGood(string s) {
        int n = s.length();

        stack<char> st;
        string result;
        int j=0;
        while(j<n){
            if(st.empty()){
                st.push(s[j]);
            }
             
             else if(!st.empty() && (s[j]-32==st.top() || s[j]+32==st.top())){
                        st.pop();
                    }
            else
            st.push(s[j]);
            j++;
        

        }
        while(!st.empty()){
            result.push_back(st.top());
            st.pop();
        }
        reverse(result.begin(),result.end());
        return result;
        
    
    }
};
