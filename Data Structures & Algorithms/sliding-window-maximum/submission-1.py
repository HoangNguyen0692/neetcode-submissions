from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        arr_len = len(nums)
        window_idx = []

        if arr_len == 1:
            return nums

        # loop through nums
        for i in range(arr_len):
            
            while window_idx and nums[window_idx[-1]] < nums[i]:
                window_idx.pop()

            window_idx.append(i)

            if i - k == window_idx[0]:
                window_idx.pop(0)
            
            #Once our window reaches size 'k', the biggest number 
            # is always sitting right at the front of our list.
            if i + 1 >= k:
                res.append(nums[window_idx[0]])
                
        return res
        