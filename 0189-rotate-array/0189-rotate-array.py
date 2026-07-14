class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        k %= n

        temp = [0] * n

        for i in range(n):
            temp[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = temp[i]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna