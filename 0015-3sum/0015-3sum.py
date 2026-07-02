class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                    # must sort first!
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1 
            k = len(nums) - 1          # right pointer
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

                elif current_sum < 0:
                    j += 1             # need bigger sum
                else:
                    k -= 1             # need smaller sum
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna