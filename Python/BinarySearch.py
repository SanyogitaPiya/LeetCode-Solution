def search(nums, target):
        if(len(nums)==0):
            return -1
        if(len(nums)==1):
            if(nums[0]==target):
                return 0
            return -1
        left = 0
        right = len(nums)-1
        mid = int(len(nums)/2)
        while(left <= right):
            if(nums[mid]<target):
                left = mid+1
                mid = int((left + right)/2) 
            elif(nums[mid] > target):
                right = mid - 1
                mid = int((left + right)/2)
            else:
                return mid
        return -1
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))