"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = []
        end = []

        for i in intervals:

            a = i.start
            b = i.end
            
            start.append(a)
            end.append(b)

        start.sort()
        end.sort()

        s = 0
        e = 0

        result = 0
        count = 0

        while s < len(intervals):

            if start[s] < end[e]:
                count += 1
                s += 1

            else:
                count -= 1
                e += 1

            result = max(result, count)

        return result
             
            