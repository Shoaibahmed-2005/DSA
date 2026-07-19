class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        i=0
        j=n-1
        while j>i:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                s[j],s[i]=s[i],s[j]
                i+=1
                j-=1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna