import heapq

def _ordered_events(events):
    """Removes Empty,Validates and Sort
    """
    valids = []
    for start,end in events:
        if start > end:
            raise ValueError("Start Must not Exceed End")
        if start < end:
            valids.append((start,end))
    return sorted(valids)

def can_attend_all(events):
    """If time overlaps its not possible to attend all"""
    ordered = _ordered_events(events)
    for i in range(1,len(ordered)):
        if ordered[i][0] < ordered[i-1][1]:
            return False
    return True

def min_rooms(events):
    ordered = _ordered_events(events)
    active_ends = []
    peak = 0
    for start,end in ordered:
        while active_ends and active_ends[0] <= start:
            heapq.heappop(active_ends)
        heapq.heappush(active_ends,end)
        peak = max(peak,len(active_ends))

    return peak

if __name__ == "__main__":
    tests = [
        ("Adjacent Meetings",[(9,10),(10,11),(11,12),(12,13)]),
        ("Overlapping Meetings",[(0,30),(5,10),(15,20),(30,40)]),
        ("No Meetings",[])
    ]

    for label,events in tests:
        print(f"{label}: {events}")
        print("Can attend all: ",can_attend_all(events))
        print("Minimum Rooms: ",min_rooms(events))

