class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        size_arr = [str(len(val)) for val in strs]

        return ",".join(size_arr) + "#" + "".join(strs)


    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        
        hash_idx = s.find("#")

        size_data = s[:hash_idx]
        real_data = s[hash_idx + 1:] # omit the #

        size_arr = [int(val) for val in size_data.split(',')]

        real_list = []
        data_idx = 0

        for size in size_arr:
            real_list.append(real_data[data_idx: (data_idx + size)])
            data_idx += size

        return real_list
