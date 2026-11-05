import heapq
import random
import time

def min_rooms(meetings):
    meetings = sorted(meetings)
    heap = []
    rooms = 0

    for start, end in meetings:
        if len(heap) > 0 and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        if len(heap) > rooms:
            rooms = len(heap)

    return rooms

def test_min_rooms():
    assert min_rooms([]) == 0
    assert min_rooms([(0,30)]) == 1
    assert min_rooms([(0,30),(5,10),(15 , 20)])== 2
    assert min_rooms([(1 , 5),(5,8),(8 , 10)])==1
    assert min_rooms([(1 , 5),(2,6),(3 , 7), (4, 8)])== 4
    assert min_rooms([(9, 11),(10,12),(11,13),(14,16), (15,17) , (15,18)])== 3
    print("All tests passed")

def experiment():
    print("n".ljust(10)+"rooms".ljust(8) + "time")
    for n in [1000,10000,100000,1000000]:
        meetings = []
        for _ in range(n):
            start = random.randint(0, n*10)
            meetings.append((start, start + random.randint(1, 100)))
        t = time.perf_counter()
        rooms = min_rooms(meetings)
        print(str(n).ljust(10)+str(rooms).ljust(8) +str(round(time.perf_counter() - t,4))+ "s")


test_min_rooms()
experiment()
