class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        max_length = 0
        current_length = 0
        seen_chars = set()
        left = 0

        for right in range(len(s)):
            
            current_char = s[right]
            current_length += 1
            
            while current_char in seen_chars:
                seen_chars.remove(s[left])
                left += 1
                current_length -= 1
                
            seen_chars.add(current_char)
            max_length = max(max_length, current_length)

        return max_length
            
