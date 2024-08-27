/*
https://leetcode.com/problems/string-compression/description/

https://www.geeksforgeeks.org/problems/run-length-encoding/1

mike
https://youtu.be/I7drewKcN1Y?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */
class Solution {
public:
    int compress(vector<char>& chars) {
        int index=0;
        int i=0;
        int length = chars.size();
        while(i<length){
            char curr = chars[i];
            int count=0;
            while(i<length && curr==chars[i]){
                i+=1;
                count++;
            }
            chars[index]=curr;
            index++;
            if(count>1){
                string count_str = to_string(count);
                for(char &ch:count_str){
                    chars[index]=ch;
                    index++;
                }
            }
        }
        return index;
    }
};

=============================================
class Solution:
    def encode(self, s : str) -> str:
        index = 0
        i = 0
        # s = list(s)
        length = len(s)
        result = ""
        while i<length:
            curr=s[i]
            count=0
            while i<length and curr==s[i]:
                i+=1
                count+=1
            result+=curr
            # s[index]=curr
            index+=1
            string = str(count)
            for each in string:
                result+=each
                
        return result
