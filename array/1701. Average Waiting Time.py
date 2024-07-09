'''
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. 
The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. 
The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

https://leetcode.com/problems/average-waiting-time/description/
'''
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        length = len(customers)
        current = 0
        result = 0
        for i in range(length):
            start = customers[i][0]
            end = customers[i][1]
            if current <=start:
                current = start
            current = current+end
            result += current-start
        return result/length
