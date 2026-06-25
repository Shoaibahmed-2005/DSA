def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k
result=removeElement([1,2,2,4,5,6],2)
print("Result count is :",result)