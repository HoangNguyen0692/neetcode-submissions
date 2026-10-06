from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return ""

        # keep track of chars in t
        t_char_track = defaultdict(int)
        for c in t:
            t_char_track[c] += 1
        maxinum_required = len(t_char_track)
        
        # to keep track of current windows
        current_char_track = defaultdict(int)
        current_matches = 0

        left = 0
        ans = (float('inf'), None, None)

        for right in range(len_s):

            current_char = s[right]
            current_char_track[current_char] += 1

            if current_char in t_char_track and current_char_track[current_char] == t_char_track[current_char]:
                current_matches += 1
            
            while left <= right and current_matches == maxinum_required:

                current_left_char = s[left]

                # save the shortest length
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # sliding left
                current_char_track[current_left_char] -= 1

                # only reduce matches if the char presents in both dicts
                if current_left_char in t_char_track and current_char_track[current_left_char] < t_char_track[current_left_char]:
                    current_matches -= 1
                
                left += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


                




        
                