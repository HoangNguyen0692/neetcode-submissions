class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len:
            return False

        s1_char_count = [0] * 26
        for i in range(s1_len):
            s1_char_count[ord(s1[i]) - ord('a')] += 1
        
        l_cur = 0
        current_char_count = [0] * 26
        for r_cur in range(s2_len):
            current_char_count[ord(s2[r_cur]) - ord('a')] += 1

            if r_cur - l_cur + 1 > s1_len:
                current_char_count[ord(s2[l_cur]) - ord('a')] -= 1
                l_cur += 1
            
            if s1_char_count == current_char_count:
                return True
        
        return False

            




        
          
