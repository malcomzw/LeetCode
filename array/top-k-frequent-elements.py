import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of the top k frequent elements
        heap = []
        
        for num, freq in freq_map.items():
            # Use heapq.heappush to add items to the heap
            heapq.heappush(heap, (-freq, num))  # push negative frequency for max-heap behavior
        
        # Step 3: Extract the top k elements from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
