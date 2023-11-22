def Cycle(nums):
    i = 0
    while i < len(nums):
        
        if i != nums[i]-1:
            temp = nums[i]
            nums[i] , nums[temp-1] = nums[temp-1] , temp
        else:
            i+=1
    return nums