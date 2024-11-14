import heapq #import heap 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) #counter
        heap = [] #heap 

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(key, val))
            else:
                heapq.heappushpop(heap, (key, val))
        return [h[1] for h in heap ]