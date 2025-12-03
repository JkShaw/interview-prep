"""
Meeting Rooms II
----------------
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
----------------
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
----------------
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
----------------
1 <= intervals.length <= 104
0 <= start-index < end-index <= 106

"""
def min_meeting_rooms(intervals):
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    rooms_needed = 0
    max_rooms_needed = 0
    start_index = 0
    end_index = 0

    while start_index < len(intervals):
        # If a meeting starts before another ends, we need a new room
        if start_times[start_index] <= end_times[end_index]:
            rooms_needed += 1

            # Update max rooms needed so far
            max_rooms_needed = max(max_rooms_needed, rooms_needed)
            start_index += 1
        else:
            end_index += 1
            rooms_needed -= 1

    return max_rooms_needed

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print(min_meeting_rooms(intervals))