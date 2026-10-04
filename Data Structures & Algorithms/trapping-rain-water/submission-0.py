class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        current_water = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                current_water += left_max - height[left]
            
            else:
                right -= 1
                right_max = max(right_max, height[right])
                current_water += right_max - height[right]
        
        return current_water