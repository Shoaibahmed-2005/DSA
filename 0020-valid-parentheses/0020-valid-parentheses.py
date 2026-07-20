class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapped={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1]!=mapped[ch]:
                    return False
                stack.pop()
        return len(stack)==0
        
            


            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna