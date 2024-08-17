'''
https://www.geeksforgeeks.org/problems/k-largest-elements4206/1
'''
import heapq

class Solution:

	def kLargest(self,arr, n, k):
		# code here
		hp = []
		for i in range(n):
		    heapq.heappush(hp,arr[i])
		    if len(hp)>k:
		        heapq.heappop(hp)
	    hp.sort(reverse=True)
	    return hp


# cpp
============================

class Solution{
public:	
	vector<int> kLargest(int arr[], int n, int k) {
	   priority_queue<int,vector<int>,greater<int>> minHeap;
	   for(int i=0;i<n;i++){
	       minHeap.push(arr[i]);
	       if(minHeap.size()>k){
	           minHeap.pop();
	       }
	   }
	   vector<int>result;
	   int length = minHeap.size();
	   while(length--){
	       result.push_back(minHeap.top());
	       minHeap.pop();
	   }
	   //revese sort
	   sort(result.rbegin(),result.rend());
	   return result;
	}

};
