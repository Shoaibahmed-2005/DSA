class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna