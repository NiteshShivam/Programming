'''
Given a matrix of size r*c. Traverse the matrix in spiral form.
'''

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        direction = 0
        top = 0
        down = len(matrix)-1
        result = []
        left =0
        right = len(matrix[0])-1
        while top<=down and left<=right:
            if direction==0:
                j=left
                while j<=right:
                    result.append(matrix[top][j])
                    j+=1
                
                top+=1
            if direction==1:
                j=top
                while j<=down:
                    result.append(matrix[j][right])
                    j+=1
            
                right-=1
            if direction==2:
                j = right
                while j>=left:
                    result.append(matrix[down][j])
                    j-=1
                
                down-=1
            if direction==3:
                j = down
                while j>=top:
                    result.append(matrix[j][left])
                    j-=1
                
                left+=1
            direction = (direction+1)%4
                
        return result
