from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return

        ref_point = ord('a')
        char_map = defaultdict(list)
        result = []

        for s in strs: 

            char_arr = [0] * 26
            cursor = 0

            while cursor < len(s):
                char_arr[ord(s[cursor]) - ord('a')] += 1
                cursor += 1
            
            char_map[tuple(char_arr)].append(s)
            
        return [val for val in char_map.values()]
            
            

            

