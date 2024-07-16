'''
https://www.geeksforgeeks.org/problems/remaining-string3515/1
'''
#User function Template for python3
class Solution:
    def printString(self, s, ch, count):
        length = len(s)
        result = 0
        for i in range(length):
            if s[i]==ch:
                count-=1
            if count==0:
                result = i+1
                break
        if count>0:
           return ""
        return s[result:]





===========================================
# c++
class Solution {
  public:

    string printString(string s, char ch, int count) {
        // Your code goes here
        int length = s.length();
        int result=0;
        for(int i=0;i<length;i++){
            if(s[i]==ch){
                count-=1;
            }
            if(count==0){
                result = i+1;
                break;
            }
        }
        if(count>0){
            return "";
        }
        return s.substr(result);
    }
};
