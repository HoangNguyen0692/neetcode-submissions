from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
    
        char_map = defaultdict(int)
        idx = 0
        
        for ch in s:
            char_map[ch] += 1

        for ch in t:
            char_map[ch] -= 1

        return all(value == 0 for value in char_map.values())

            