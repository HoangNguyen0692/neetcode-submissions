class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        len_numbs = len(numbers)
        if len_numbs == 2:
            return [1, 2]

        left, right = 0, len_numbs - 1

        while left < right:
            
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
            


