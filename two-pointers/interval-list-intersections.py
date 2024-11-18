class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #pointers for both lists of intervals 
        i, j = 0, 0 
        result = [] #result to store the intervals 
        
        #iterate the 2 lists if valid 
        while i < len(firstList) and j< len(secondList):
            #while valid , lets do processing 
            #calculate the possible intersection points 
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            #if the intersections are valid 
            #add to the final result 
            if start<= end:
                result.append([start, end ])

            #move the pointer of the interval that ends first 
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else :
                j +=1
        return result 

