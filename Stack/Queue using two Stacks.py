'''
https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1
'''
def Push(x,stack1,stack2):
    stack1.append(x)


def Pop(stack1,stack2):
    if stack2:
        return stack2.pop()
    else:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        return -1
    return stack2.pop()
