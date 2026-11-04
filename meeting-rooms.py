import heapq


def min_rooms(meetings):
    meetings.sort()
    heap = []
    rooms = 0

    for start, end in meetings:
        if len(heap) > 0 and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        if len(heap) > rooms:
            rooms = len(heap)

    return rooms

meetings = [(9, 11), (10, 12), (11, 13), (14, 16), (15, 17), (15, 18)]

print("Meetings:", meetings)
print("Minimum rooms needed:", min_rooms(meetings))


