class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [None, None]

        seen = {}
        rest  = 0

        for pos, num in enumerate(nums):
            rest = target - num

            if rest in seen:
                return [seen[rest], pos]
            
            seen[num] = pos
      
        return [None, None]

