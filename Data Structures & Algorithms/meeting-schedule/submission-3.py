"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        true/false if can attend all meetings
        find overlaps -> true if none

        sort by start time
        check if nextStart < prevEnd

        0   5   10  15  20  25  30
        --------------------------
            -----
                    ------
        
              ---
         ----
        """

        intervals.sort(key=lambda i: i.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True