
def twoSum(nums, target):
    if len(nums) == 2 :
        return [0,1]
    nums_arr = sorted(nums)
    s = nums_arr[0]
    l = nums_arr[len(nums_arr)-1]
    j = 2
    i = 1
    while s+l != target :
        if s+l > target:
            l = nums_arr[len(nums_arr)-j]
            j = j+1
        elif s+l < target:
            s=nums_arr[i]
            i= i+1
    index1 = -1
    index2 = -1
    for a in range(0,len(nums)):
        if s == nums[a] and index1 == -1:
            index1 = a
        elif l == nums[a] and index2 == -1:
            index2 = a
    
    return [index1,index2]
    

nums = [3,1,3]
tar = 6
print(twoSum(nums,tar))
