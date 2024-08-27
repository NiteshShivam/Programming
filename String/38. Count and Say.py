#User function Template for python3
# https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1
# https://leetcode.com/problems/count-and-say/description/

'''
mik video
https://youtu.be/5uJitfSM3vk?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
'''
class Solution:

    def lookandsay(self, n):
        result = "1"
        n=n-1
        while n:
            # print(n)
            temp =""
            count =0
            curr=""
            for i in range(len(result)):
                if curr!=result[i]:
                    if count:
                        temp = temp + str(count)+curr
                        count=1
                        curr=result[i]
                    else:
                        count=1
                        curr = result[i]
                else:
                    count+=1
            if count:
                temp=temp+str(count)+curr
            # print(temp)
            result=temp
            # print(result)
            n-=1
        return result




================================
class Solution {
public:
    string countAndSay(int n) {
        if(n==1){
            return "1";
        }
        string result = "";
        string say = countAndSay(n-1);
        for(int i=0;i<say.length();i++){
            char ch=say[i];
            int count=1;
            while(i<say.length()-1 && say[i]==say[i+1]){
                count++;
                i++;
            }
            result += to_string(count)+string(1,ch);

        }
        return result;
    }
};
