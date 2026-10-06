import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # probably max heap

        # coordinates
        x, y = 0, 0
        max_heap = []

        for p in points:
            x, y = p
            pos_data = (-(x**2 + y**2), [x, y])

            if len(max_heap) < k:
                heapq.heappush(max_heap, pos_data)
            else:
                # The heap is full (size K). 
                # Check if the new postion is strictly greater than the root
                if pos_data[0] > max_heap[0][0]:
                    heapq.heapreplace(max_heap, pos_data)
        
        return [p[1] for p in max_heap]


        