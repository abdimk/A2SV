
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0          # window is [left, right)
        curr_sum = 0       # sum of nums[left..right-1]
        count = 0

        while left < n:
            # Extend right as far as valid
            while right < n and (curr_sum + nums[right]) * (right - left + 1) < k:
                curr_sum += nums[right]
                right += 1

            # All subarrays starting at left and ending before right are valid
            count += right - left

            # Slide window forward
            if right == left:
                # Couldn't include nums[left] at all
                right += 1
            else:
                curr_sum -= nums[left]

            left += 1

        return count