class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned="".join(char.lower() for char in s if char.isalnum())
        i=0
        j=len(cleaned)-1
        while j>i:
            if cleaned[i]!=cleaned[j]:
                return False
            i+=1
            j-=1

        return True
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna