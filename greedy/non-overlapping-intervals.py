class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #first sort the intervals with order 
        intervals.sort()

        #track the result of total removals 
        res =0
        prevEnd = intervals[0][1]

        for start , end in intervals[1:]:
            if start >= prevEnd :
                prevEnd = end 
            else :
                res+= 1
                prevEnd = min(end , prevEnd)
        return res