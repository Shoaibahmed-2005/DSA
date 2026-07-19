class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1 #visits all valid values in arr 1
        j=n-1 #visits all values in arr 2
        k=m+n-1 #its the length of the full arr 1 including 0's

        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k]=nums1[i]
                k-=1
                i-=1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna