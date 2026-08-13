import heapq
class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        if len(self.high) != 0 and num >= self.high[0]:
            heapq.heappush(self.high, num)
        else:
            heapq.heappush(self.low, -1* num)
        if len(self.low) > len(self.high) + 1:
            n = -1 * heapq.heappop(self.low)
            heapq.heappush(self.high, n)
        if len(self.low) + 1 < len(self.high):
            n =  heapq.heappop(self.high)
            heapq.heappush(self.low, -1 * n)

        

    def findMedian(self) -> float:
        # print(self.low)
        # print(self.high)
        if len(self.low) == len(self.high):
            return (-1 * self.low[0] + self.high[0]) / 2
        elif len(self.low) > len(self.high):
            return -1 * self.low[0]
        else:
            return self.high[0]
        
        