def SingleNumber(nums):
    if len(nums)==1:
        return nums[0]
    num_arr = sorted(nums)
    print(num_arr)
    if num_arr[0]!=num_arr[1] :
        return num_arr[0]
    for i in range(0, len(num_arr), 2):
        if i == len(num_arr)-1:
            return num_arr[i]
        elif num_arr[i] != num_arr [i+1] :
            number = num_arr[i]
            print(num_arr[i],num_arr[i+1])
            return number
    return -1

nums = [-336,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
print(SingleNumber(nums))