import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # O(1) space: mutate the array in-place
        for i in range(len(stones)):
            stones[i] *= -1

        # rearrange stones to heap structure
        heapq.heapify(stones)
        
        while len(stones) > 1:
            
            # pop the smallest item
            smallest = heapq.heappop(stones)
            second_smallest = heapq.heappop(stones)

            # push the diff back in if dff != 0, diff will also be negative here, but it will probably not in [0]
            if smallest != second_smallest:
                heapq.heappush(stones, smallest - second_smallest)

        return abs(stones[0]) if stones else 0
                



