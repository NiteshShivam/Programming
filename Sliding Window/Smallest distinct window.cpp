// https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1
class Solution{
    public:
    int findSubString(string str)
    {
        int result=INT_MAX;
        vector<int> space(256,0);
        int unique=0;
        
        for(int right=0;right<str.size();right++){
            int index = str[right];
            space[index]++;
            if(space[index]==1){
                unique++;
            }
        }
        for(int i =0;i<256;i++){
            space[i]=0;
        }
        
        int left=0;
        int current=0;
        for(int right=0;right<str.size();right++){
            space[str[right]]+=1;
            if(space[str[right]]==1){
                current+=1;
            }
            while(current==unique){
                space[str[left]]--;
                if(space[str[left]]==0){
                    current--;
                }
                result = min(result,right-left+1);
                left++;
            }
        }
        
        return result;
    }
};


// python
================

class Solution:
    def findSubString(self, str):
        unique = len(set(str))
        
        space = [0]*256
        count = 0
        left=0
        result = float('inf')
        for right in range(len(str)):
            space[ord(str[right])]+=1
            if space[ord(str[right])]==1:
                count+=1
            while count==unique:
                space[ord(str[left])]-=1
                if space[ord(str[left])]==0:
                    count-=1
                result = min(result,right-left+1)
                left+=1
                
        return result
