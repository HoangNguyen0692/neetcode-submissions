import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # convert stones to negative stones
        neg_stones = [-x for x in stones]

        # rearrange stones to heap structure
        heapq.heapify(neg_stones)
        
        while len(neg_stones) > 1:
            
            # pop the smallest item
            smallest = heapq.heappop(neg_stones)
            second_smallest = heapq.heappop(neg_stones)

            # push the diff back in if dff != 0, diff will also be negative here, but it will probably not in [0]
            diff = smallest - second_smallest
            if diff != 0:
                heapq.heappush(neg_stones, diff)

        return abs(neg_stones[0]) if neg_stones else 0
                



