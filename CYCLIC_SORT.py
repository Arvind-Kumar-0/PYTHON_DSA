def Cycle(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]-1
        if correct<len(nums) and nums[i] != nums[correct]:
            nums[i] , nums[correct] = nums[correct] , nums[i]
        else:
            i+=1
    return nums

nums = [6,3,2,5,4,1]

Cycle(nums)