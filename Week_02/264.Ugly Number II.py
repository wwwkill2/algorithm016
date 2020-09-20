from heapq import heappop, heappush
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heappush(heap, 1)
        count = 0
        while True:
            res = heappop(heap)
            count += 1
            if count == n:
                return res
            while heap != [] and res == heap[0]:
                heappop(heap)
            heappush(heap, res * 2)
            heappush(heap, res * 3)
            heappush(heap, res * 5)
