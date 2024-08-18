'''
https://leetcode.com/problems/ugly-number-ii/description/
https://youtu.be/jRacRh6x4go
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0]*n
        two = 0
        three = 0
        five = 0
        ugly[0]=1
        
        for i in range(1,n):
            next2,next3,next5 = ugly[two]*2,ugly[three]*3,ugly[five]*5
            next_ugly = min(next2,next3,next5)
            ugly[i]=next_ugly
            if next2==next_ugly:
                two+=1
            if next3==next_ugly:
                three+=1
            if next5==next_ugly:
                five+=1

        return ugly[-1]


# cpp
==================================
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n+1,0);
        dp[0]=1;
        int two=0,three=0,five=0;
        for(int i=1;i<=n;i++){
            int first = dp[two]*2;
            int second = dp[three]*3;
            int third = dp[five]*5;
            int value = min({first,second,third});
            //cout<<" "<<value<<endl;
            if(value==first){
                two++;
            }
            if(value==second){
                three++;
            }
            if(value==third){
                five++;
            }
            dp[i]=value;
        }
        return dp[n-1];
    }
};
