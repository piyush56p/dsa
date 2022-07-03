class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            top = 0
            down = len(matrix) #3
            left = 0
            right = len(matrix[0]) #4
            a = []
            direction = 0
            while(top<down and right>left):

                    for i in range(left,right):
                        a.append(matrix[top][i])
                    top+=1 #1

                    for j in range(top,down):
                        a.append(matrix[j][right-1])
                    right-=1 #3 
                    if not(left<right and top<down):
                        break


                    for k in range(right-1,left-1,-1):
                        a.append(matrix[down-1][k])
                    down-=1

                    for i in range(down-1, top-1,-1):
                        a.append(matrix[i][left])
                    left+=1
            return a
