#双一百
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        i = 0
        for j in range(1, len(intervals)):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[j][1], intervals[i][1])
            else:
                i = i+1
                if i!=j:
                    intervals[i] = intervals[j]
            if j == len(intervals)-1:
                return intervals[0:i+1]
