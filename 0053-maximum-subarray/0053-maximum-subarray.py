class Solution:
    def maxSubArray(self, nums):

        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):

            currSum = max(nums[i], currSum + nums[i])

            maxSum = max(maxSum, currSum)

        return maxSum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna