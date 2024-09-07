/*
https://leetcode.com/problems/delete-columns-to-make-sorted/description/
mik-video:
https://youtu.be/tFQWBeljuaU?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int slength = strs[0].size();
        int count=0;
        for(int j=0;j<slength;j++){
            char ch = strs[0][j];
            for(int i=1;i<n;i++){
                if(ch<=strs[i][j]){
                    ch=strs[i][j];
                }
                else{
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};
