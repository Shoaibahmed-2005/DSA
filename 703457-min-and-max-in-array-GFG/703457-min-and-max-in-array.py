class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]
        for num in arr:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        return minimum, maximum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna