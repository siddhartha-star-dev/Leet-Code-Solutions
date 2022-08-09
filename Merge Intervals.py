class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        i=0
        if len(intervals)<2:
            return intervals
        while(i<(len(intervals)-1)):
            while(i<(len(intervals)-1) and intervals[i+1][0]<=intervals[i][1]):
                lower_lim = intervals[i][0]
                upper_lim = max(intervals[i][1],intervals[i+1][1])
                del intervals[i+1]
                intervals[i] = [lower_lim,upper_lim]
            i+=1
        return intervals
