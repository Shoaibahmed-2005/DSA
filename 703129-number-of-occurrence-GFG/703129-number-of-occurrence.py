class Solution:

    def countFreq(self, arr, target):

        first = self.findFirst(arr, target)

        if first == -1:
            return 0

        last = self.findLast(arr, target)

        return last - first + 1


    def findFirst(self, arr, target):

        left = 0
        right = len(arr) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] == target:
                ans = mid
                right = mid - 1

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans


    def findLast(self, arr, target):

        left = 0
        right = len(arr) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] == target:
                ans = mid
                left = mid + 1

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna