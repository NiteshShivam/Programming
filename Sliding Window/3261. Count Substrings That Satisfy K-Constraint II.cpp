/*
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/description/
https://youtu.be/2d1ALG8wwDc
  */
class Solution {
public:
    vector<long long> countKConstraintSubstrings(string s, int k, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> leftMost(n,0);
        vector<int> rightMost(n,0);
        int i=0;
        int j=0;
        int zero=0;
        int one = 0;
        while(j<n){
            if(s[j]=='0'){
                zero+=1;
            }
            else{
                one+=1;
            }
            while(zero>k && one>k){
                if(s[i]=='0'){
                    zero--;
                }
                else{
                    one--;
                }
                i++;
            }
            leftMost[j] = i;
            j+=1;
        }
        i = n-1;
        j=n-1;
        zero=0;
        one =0;

        while(j>=0){
            if(s[j]=='0'){
                zero++;
            }
            else{
                one++;
            }
            while(zero>k && one>k){
                if(s[i]=='0'){
                    zero--;
                }
                else{
                    one--;
                }
                i-=1;
            }
            rightMost[j]=i;
            j-=1;
        }
        vector<int>tempValid(n,0);
        for(int j=0;j<n;j++){
            tempValid[j] = j-leftMost[j]+1;
        }
        vector<long long> cumSum(n,0);
        cumSum[0]=tempValid[0];
        for(int j=1;j<n;j++){
            cumSum[j] = cumSum[j-1]+tempValid[j];
        }
        vector<long long>result;
        for(vector<int>& q : queries){
            int low = q[0];
            int high=q[1];
            int validIndex = min(high,rightMost[low]);
            long long length = validIndex-low+1;
            long long tempResult = length*(length+1)/2;
            tempResult+=cumSum[high]-cumSum[validIndex];
            result.push_back(tempResult);
        }

        return result;
    }
};
