import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counter = Counter(tasks)

        # add time to heap
        max_heap = [-val for val in task_counter.values()]
        heapq.heapify(max_heap)

        # prepare cooldown queue
        cooldown_queue = deque()
        time = 0 # cycle count
        
        while max_heap or cooldown_queue:
            # Tick the clock at the start of the CPU cycle
            time += 1
        
            if max_heap:
                current_count = heapq.heappop(max_heap)
                current_count += 1 # the count is negative here to ensure the first position in heap

                # Indented inside so we only queue it if we actually popped it
                if current_count < 0: # negative
                    # time + n is the exact cycle it finishes cooling down
                    cooldown_queue.append((current_count, time + n))

            
            # 2. RELEASE phase (FIX 3)
            # Check the front of the queue to see if the wake-up time matches the current time
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_task = cooldown_queue.popleft()
                # Push the count (index 0 of the tuple) back into the heap
                heapq.heappush(max_heap, ready_task[0])

        # When the while loop finally breaks, 'time' holds exactly how many cycles ran!
        return time






        