class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #declare the result array to hold the output of intervals 
        result = []

        #iterate all intervalls given to check where to insert the new interval 
        for i in range(len(intervals)):
            #check if the intervals overlap or dont 
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval) 
                return result + intervals[i:]
            #if they overlap
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else :
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)

        return result 