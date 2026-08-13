import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.heap, n)

        while len(self.heap) > k:
            n = heapq.heappop(self.heap)
            # print(n)
        
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if val > self.heap[0]:
            n = heapq.heappop(self.heap)

            heapq.heappush(self.heap, val)
            # print(n)
            # print(val)
            return self.heap[0]
        else:
            return self.heap[0]
        
