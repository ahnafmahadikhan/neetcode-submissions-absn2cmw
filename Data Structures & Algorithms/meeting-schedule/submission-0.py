"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):

            a = intervals[i].start
            b = intervals[i].end

            c = intervals[i - 1].start
            d = intervals[i - 1].end

            if a < d:
                return False

        return True