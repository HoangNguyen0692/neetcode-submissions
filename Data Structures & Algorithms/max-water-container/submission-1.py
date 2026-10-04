class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        max_surface = 0

        while left < right:

            current_surface = (right - left) * min(heights[left], heights[right])
            if max_surface < current_surface:
                max_surface = current_surface

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_surface



        