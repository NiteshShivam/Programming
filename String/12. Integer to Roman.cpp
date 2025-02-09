/*
https://leetcode.com/problems/integer-to-roman/description/
https://www.geeksforgeeks.org/problems/convert-to-roman-no/1

mik video
https://youtu.be/2FPvU8XmsKU?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */
class Solution {
public:
    string intToRoman(int num) {
        vector<int> val{1000,900,500,400,100,90,50,40,10,9,5,4,1};
        vector<string> sym{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        string result="";
        for(int i=0;i<13;i++){
            if(num==0){
                break;
            }
            int times = num/val[i];
            while(times--){
            result.append(sym[i]);
            }
            num = num%val[i];
        }
        return result;

    }
};




===========================
 
class Solution:
    def convertRoman(self, n):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        string = ["M",'CM','D','CD','C','XC','L','XL','X',"IX",'V','IV','I']
        result = ""
        for i in range(13):
            if not n:
                break
            times = n//val[i]
            while times>0:
                result +=string[i]
                times-=1
            n = n%val[i]
        return result
