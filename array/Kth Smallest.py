'''
https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
'''
import heapq
class Solution:

    def kthSmallest(self, arr,k):
        hp = []
        for each in arr:
            heapq.heappush(hp,-each)
            if len(hp)>=(k+1):
                heapq.heappop(hp)
        return -heapq.heappop(hp)
        

# cpp
==================================
class Solution {
  public:
    // arr : given array
    // k : find kth smallest element and return using this function
    int kthSmallest(vector<int> &arr, int k) {
        priority_queue<int> maxHeap;
        for(int i=0;i<arr.size();i++){
            maxHeap.push(arr[i]);
            if(maxHeap.size()>k){
                maxHeap.pop();
            }
        }
        return maxHeap.top();
    }
};


# using partion quick sort
===============


class Solution:
    def partition(self,arr,l,r,pivot):
        arr[l+pivot],arr[r] = arr[r],arr[l+pivot]
        i = l
        j = l-1
        while i<r:
            if arr[i]<arr[r]:
                j+=1
                arr[i],arr[j]=arr[j],arr[i]
            i+=1
        arr[j+1],arr[r] = arr[r],arr[j+1]
        return j+1
    def kthSmallest(self, arr,k):
        l =0
        r=len(arr)-1
        
        while l<=r:
            pivot = (r-l)//2
            result = self.partition(arr,l,r,pivot)
            if result==k-1:
                return arr[result]
            elif result>k-1:
                r=result-1
            else:
                l=result+1
        return -1
