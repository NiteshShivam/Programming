Given two singly linked lists of size N and M, 
write a program to get the point where two linked lists intersect each other.



Approach 1 not passing all test cases:


from collections import deque
#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #
    stack1 = deque()
    stack2 = deque()
    while head1:
        stack1.append(head1)
        head1 = head1.next
    while head2:
        stack2.append(head2)
        head2 = head2.next
    result = -1
    while stack1 and stack2:
        first = stack1.pop()
        second = stack2.pop()
        if first.data==second.data:
            result = first.data
            
        else:
            break
    return result

Approach 2: passing all test cases:
def intersetPoint(head1,head2):
    #
    storage = set()
    while head1:
        storage.add(head1)
        head1=head1.next
    while head2:
        if head2 in storage:
            return head2.data
        head2 = head2.next
    return -1


Approach 3: O(1) space
def intersetPoint(head1,head2):
    count1 =0
    count2 = 0
    temp = head1
    while temp:
        count1+=1
        temp = temp.next
    temp = head2
    while temp:
        count2+=1
        temp = temp.next
    temp1 = head1
    temp2 = head2
    if count1>count2:
        while count1>count2:
            temp1=temp1.next
            count1-=1
    else:
        while count1<count2:
            temp2=temp2.next
            count2-=1
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1.data
        temp1 =temp1.next
        temp2 = temp2.next
    return -1


Approach 4 (Optimal) :
https://youtu.be/0DYoPz2Tpt4
#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    if not head1 or not head2:
        return -1
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        temp1 =temp1.next
        temp2 = temp2.next
        if temp1==temp2:
            if not temp1:
                return -1
            return temp1.data
        if not temp1:
            temp1 = head2
        if not temp2:
            temp2 = head1
    return -1
