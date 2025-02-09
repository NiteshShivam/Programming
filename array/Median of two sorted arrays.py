'''
https://www.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1

https://youtu.be/6D9T2ZY8h5c
https://youtu.be/7nABqJCEMuY
'''
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        length1 = len(arr1)
        length2 = len(arr2)
        temp = []
        i=0
        j=0
        while i<length1 and j<length2:
            if arr1[i]<arr2[j]:
                temp.append(arr1[i])
                i+=1
            else:
                temp.append(arr2[j])
                j+=1
        while i<length1:
            temp.append(arr1[i])
            i+=1
        while j<length2:
            temp.append(arr2[j])
            j+=1
        result = 0
        if (length1+length2)%2==0:
            t = (length1+length2)//2
            result = temp[t]+temp[t-1]
        else:
            t = (length1+length2)//2
            result = temp[t]
        return result



=========================
#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        length1 = len(arr1)
        length2 = len(arr2)
        t1  = (length1+length2)//2
        t2 = t1-1
        ans1= 0
        ans2=0
        i=0
        j=0
        k = 0
        while i<length1 and j<length2:
            if arr1[i]<arr2[j]:
                if k==t1:
                    ans1=arr1[i]
                elif k==t2:
                    ans2 = arr1[i]
                k+=1
                i+=1
            else:
                if k==t1:
                    ans1=arr2[j]
                elif k==t2:
                    ans2 = arr2[j]
                k+=1
                j+=1
                
                
        while i<length1:
            if k==t1:
                ans1=arr1[i]
            elif k==t2:
                ans2 = arr1[i]
            k+=1
            i+=1
        while j<length2:
            if k==t1:
                ans1=arr2[j]
            elif k==t2:
                ans2 = arr2[j]
            k+=1
            j+=1
        result = 0
        if (length1+length2)%2==0:
            result = ans1+ans2
        else:
           
            result = ans1
        return result



================================
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        if len(arr1)>len(arr2):
            return self.sum_of_middle_elements(arr2, arr1)
        m = len(arr1)
        n = len(arr2)
        l = 0
        r =m
        while l<=r:
            px = l+(r-l)//2
            py = (m+n+1)//2-px
            x1 = arr1[px-1] if px>0 else float('-inf')
            x2 = arr2[py-1] if py>0 else float('-inf')
            x3 = arr1[px] if px<m else float('inf')
            x4 = arr2[py] if py<n else float('inf')
            
            if x1<=x4 and x2<=x3:
                if (m+n)%2==0:
                    return max(x1,x2)+min(x3,x4)
                else:
                    return max(x1,x2)
            if x1>x4:
                r = px-1
            else:
                l = px+1
        return -1






# cpp
=======================
class Solution{
    public:
    double MedianOfArrays(vector<int>& array1, vector<int>& array2)
    {
        if(array1.size()>array2.size())
            return MedianOfArrays(array2,array1);
        int m = array1.size();
        int n = array2.size();
        int l = 0;
        int r=m;
        while(l<=r){
            int px = l+(r-l)/2;
            int py = (m+n+1)/2-px;
            int x1 = (px>0)?array1[px-1]:INT_MIN;
            int x2= (py>0)?array2[py-1]:INT_MIN;
            int x3 = (px<m)?array1[px]:INT_MAX ;
            int x4 = (py<n)?array2[py]:INT_MAX ;
            if(x1<=x4 && x2<=x3){
                if((m+n)%2==0)
                {
                    return (max(x1,x2) + min(x3,x4) )/2.0;
                }
                return max(x1,x2);
            }
            if(x1>x4){
                r = px-1;
            }
            else{
                l = px+1;
            }
        
        }
        return -1;
    
    }
};


