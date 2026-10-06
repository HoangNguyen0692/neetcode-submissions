import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # Notice we don't even need to save self.nums. 
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        
        if len(self.min_heap) < self.k:
            # If we haven't reached K trades yet, just push it in.
            heapq.heappush(self.min_heap, val)
        else:
            # The heap is full (size K). 
            # Check if the val is strictly greater than 
            # the smallest val currently in our Top K (which is at index 0).
            if val > self.min_heap[0]:
                # heapreplace() efficiently pops the smallest item and pushes the new one
                # in a single, atomic O(log K) operation.
                heapq.heapreplace(self.min_heap, val)

        # The Kth largest overall is the SMALLEST of the Top K elements.
        # In a Min-Heap, the smallest element is ALWAYS at index 0.
        return self.min_heap[0]

