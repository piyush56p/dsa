class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
            
        maxUnits = 0
        for numberofBoxes, unitsperBox in boxTypes:
            takeboxes = min(truckSize, numberofBoxes)
            truckSize -= takeboxes
            maxUnits += takeboxes*unitsperBox
        return maxUnits
            
        
