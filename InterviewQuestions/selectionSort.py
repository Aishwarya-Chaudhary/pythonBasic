def sort(nums):
    for i in range(6):
        minpos = i
        for j in range(i,7):
            if nums[j]<nums[minpos]:
                minpos=j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

nums=[8,2,4,25,1,3,9]
sort(nums)
print(nums)