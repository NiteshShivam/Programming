/*
https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1
  */
class Solution {
  public:
    int smallestSubstring(string S) {
       int result =INT_MAX;
       int left=0;
       int right=0;
       
    
       int zero=0;
       int one=0;
       int two=0;
       
       for(int right=0;right<S.size();right++){
           if(S[right]=='0'){
               zero++;
           }
           else if(S[right]=='1'){
               one++;
           }
           else if(S[right]=='2'){
               two++;
           }
           while(zero!=0 && one!=0 && two!=0){
               result = min(result,right-left+1);
               if(S[left]=='0'){
                   zero--;
               }
               else if(S[left]=='1'){
                   one--;
               }
               else if(S[left]=='2'){
                   two--;
               }
               left++;
           }
           }
        if(result==INT_MAX){
            return -1;
        }
        return result;
        
    }
       
       
};
