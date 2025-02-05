def sort(nums):
    for i in range(len(nums)-1,0,-1): #we move 0-5 index .And in bubble sort we sort the last list value first
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j + 1]=temp

nums=[4,7,3,0,2,8]
sort(nums)
print(nums)