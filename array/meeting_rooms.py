def min_meeting_rooms(intervals):
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    rooms_needed = 0
    max_rooms_needed = 0
    start_index = 0
    end_index = 0

    while start_index < len(intervals):
        # If a meeting starts before another ends, we need a new room
        if start_times[start_index] < end_times[end_index]:
            rooms_needed += 1

            # Update max rooms needed so far
            max_rooms_needed = max(max_rooms_needed, rooms_needed)
            start_index += 1

        else:
            # Meeting has ended, so free up a room
            rooms_needed -= 1
            end_index += 1

    return max_rooms_needed


if __name__ == '__main__':
    intervals = [[0,30],[5,10],[15,20]]
    result = min_meeting_rooms(intervals)
    print(result)