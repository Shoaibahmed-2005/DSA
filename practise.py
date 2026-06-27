def remove_element(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
result=remove_element([1,2,2,3,4,5],2)
print(result)
