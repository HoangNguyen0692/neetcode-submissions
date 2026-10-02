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

            for char in s:
                char_arr[ord(char) - ord('a')] += 1
            
            char_map[tuple(char_arr)].append(s)
            
        return [val for val in char_map.values()]
            
            

            

