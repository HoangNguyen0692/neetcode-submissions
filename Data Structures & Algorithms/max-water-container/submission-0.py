class Solution:
    def maxArea(self, heights: List[int]) -> int:

        h_len = len(heights)
        left, right = 0, h_len - 1
        max_surface = 0

        while left < right:

            current_width = right - left
            current_height = min(heights[left], heights[right])
            current_surface = current_width * current_height
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



        