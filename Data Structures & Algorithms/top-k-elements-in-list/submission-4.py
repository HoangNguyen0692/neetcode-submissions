class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or len(nums) <= k:
            return nums
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        return sorted(count, key=count.get, reverse=True)[:k]
