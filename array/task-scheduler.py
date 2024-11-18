class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Use a max-heap to track task frequencies (negative to simulate max-heap)
        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)
        
        time = 0  # Total time required
        
        # Process tasks while there are tasks in the heap
        while max_heap:
            temp = []  # Tasks processed in this cycle
            for _ in range(n + 1):  # Process up to (n + 1) tasks
                if max_heap:
                    temp.append(heappop(max_heap))
            
            # Add back tasks with remaining counts
            for count in temp:
                if count + 1 < 0:  # Only add back if there's more of the task left
                    heappush(max_heap, count + 1)
            
            # If heap is empty, add the actual number of tasks processed; else, add (n + 1)
            time += n + 1 if max_heap else len(temp)
        
        return time
