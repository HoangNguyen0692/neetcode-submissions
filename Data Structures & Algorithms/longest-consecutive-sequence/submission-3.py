class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if this number is the START of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count upwards as long as consecutive numbers exist
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update our record if this streak is the longest we've seen
                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak


