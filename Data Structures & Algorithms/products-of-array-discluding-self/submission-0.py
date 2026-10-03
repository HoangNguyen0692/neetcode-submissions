class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr_len = len(nums)
        prefix_arr = [1] * arr_len
        suffix_arr = [1] * arr_len
        final_arr = [0] * arr_len

        for i in range(1, arr_len):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]

        for i in range(arr_len-2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] * nums[i+1]

        for i in range(arr_len):
            final_arr[i] = prefix_arr[i] * suffix_arr[i]

        return final_arr
            

