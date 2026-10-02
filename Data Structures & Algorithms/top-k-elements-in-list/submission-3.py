from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or len(nums) <= k:
            return nums
        
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1
        
        return sorted(num_map, key=num_map.get, reverse=True)[:k]
