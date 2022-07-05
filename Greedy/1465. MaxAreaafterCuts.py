class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        lengthx = [0]
        lengthy = [0]
        lengthx = lengthx + horizontalCuts
        lengthy = lengthy + verticalCuts
        lengthx.append(h)
        lengthy.append(w)
        lengthx.sort(reverse=True)
        lengthy.sort(reverse=True)
        diffx = 0
        diffy = 0
        for i in range(len(lengthx)-1):
            
            diffx = max(diffx, lengthx[i] - lengthx[i+1] )
        for j in range(len(lengthy)-1):
            
            diffy = max(diffy, lengthy[j] - lengthy[j+1])
        area = (diffx * diffy)%(10**9+7)
        return area
