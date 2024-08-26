/*

https://leetcode.com/problems/find-the-closest-palindrome/description/

mike video
https://youtu.be/TOqxzXrSAPY
  */

class Solution {
public:
    long func(long firstHalfNum,bool isEven ){
        long result=firstHalfNum;
        if(isEven==false){
            firstHalfNum /=10;
        }
         while(firstHalfNum){
            result= result*10 + firstHalfNum%10;
            firstHalfNum /=10;
            }
        
        return result;
    }
    string nearestPalindromic(string s) {
        int L = s.length();
        int mid = L/2;
        
        int halfLength = (L%2==0)?mid:mid+1;
        long firstHalfNum = stol(s.substr(0,halfLength));
        vector<long> possibleResult;
        possibleResult.push_back(func(firstHalfNum,L%2==0));
        possibleResult.push_back(func(firstHalfNum+1,L%2==0));
        possibleResult.push_back(func(firstHalfNum-1,L%2==0));
        possibleResult.push_back((long)pow(10,L-1)-1);
        possibleResult.push_back((long)pow(10,L)+1);

        long diff=LONG_MAX;
        long result=INT_MAX;
        long OriginalNum = stol(s);
        for(long num:possibleResult){
            if(num==OriginalNum){
                continue;
            }
            if(abs(num-OriginalNum)<diff){
                result=num;
                diff=abs(num-OriginalNum);
            }
            else if(abs(num-OriginalNum)==diff){
                result = min(result,num);
            }

        }
        return to_string(result);

    }
};
