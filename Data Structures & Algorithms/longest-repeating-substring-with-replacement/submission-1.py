class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_counts = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            current_char = s[right]
            
            # 1. Add the new character to our tracker
            if current_char not in char_counts:
                char_counts[current_char] = 0
            char_counts[current_char] += 1
            
            # 2. While the window is invalid, shrink it!
            # Invalid means: (Window Length) - (Most Frequent Letter Count) > k
            while (right - left + 1) - max(char_counts.values()) > k:
                # Remove the leftmost character's count
                char_counts[s[left]] -= 1
                # Move the left pointer forward
                left += 1
                
            # 3. Now the window is guaranteed to be valid, so record its size
            max_length = max(max_length, right - left + 1)

        return max_length
            

