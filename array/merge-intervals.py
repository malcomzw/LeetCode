class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #step1 , sort the intervals 
        intervals.sort(key= lambda i :i[0])
        merged = [intervals[0]]

        #step 2 iterate all of them checking overlaps
        for start, end in intervals:
            lastEnd = merged[-1][1]

        #3 , if overlap merge , if no overlap , append 
            if start<= lastEnd :
                merged[-1][1]  = max(merged[-1][1] , end )
            else :
                merged.append([start, end])
        #return merged 
        return merged