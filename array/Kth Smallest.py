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
