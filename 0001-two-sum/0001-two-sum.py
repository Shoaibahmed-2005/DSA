class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for i in range (len(nums)):
            complement=target-nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]=i

        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna