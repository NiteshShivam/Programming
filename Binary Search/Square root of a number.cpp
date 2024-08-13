/*
https://www.geeksforgeeks.org/problems/square-root/1
https://youtu.be/Bsv3FPUX_BA

  */
class Solution {
  public:
    long long int floorSqrt(long long int n) {
        long long int left=0;
        long long int right =n;
        long long int ans =1;
        while(left<=right)
        {
            long long int mid = left+(right-left)/2;
            if(mid*mid==n){
                ans = mid;
                break;
            }
            else if(mid*mid<n){
                ans = mid;
                left=mid+1;
            }
            else{
                right=mid-1;
            }
            
        }
        // Your code goes here
        return ans;
    }
};
