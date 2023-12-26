def subset(nums: list[int],ans: list[int]=[]):
    if len(nums) <= 0:
        if ans != []:
            return [ans]
        else:
            return ans
    first = [nums[0]]
    nums =nums[1:]
    return subset(nums,ans+first) + subset(nums,ans)

print(subset([1,2,3]))

#[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3]] :=> Output
