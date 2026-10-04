class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        arr_len = len(nums)

        for anchor in range(len(nums)):

            if nums[anchor] > 0:
                break

            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue

            left, right = anchor + 1, arr_len - 1

            while left < right:
                current_sum = nums[anchor] + nums[left] + nums[right]

                if current_sum == 0:
                    res.append([nums[anchor], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif current_sum > 0:
                    right -= 1

                else: 
                    left += 1


        return res           

            
        