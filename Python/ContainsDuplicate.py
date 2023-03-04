def containsDuplicate(nums) :
    if len(nums) == 1 or len(nums) == 0:
        return False
    elif len(nums) == 2 and nums[0]!=nums[1]:
        return False
    my_dict = {}
    for i in range(0,len(nums)):
        if(nums[i] in my_dict):
            return True
            #my_dict[nums[i]] = my_dict[nums[i]]+1
        else:
            my_dict[nums[i]]=1
    #for key, value in my_dict.items():
    #    print(key, value)
    return False


nums = [1,2,4,2]
print(containsDuplicate(nums))