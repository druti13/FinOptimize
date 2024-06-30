import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def pop(self):
        return -heapq.heappop(self.heap)

    def top(self):
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)
