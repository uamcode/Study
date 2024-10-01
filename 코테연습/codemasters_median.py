def find_median(nums):
    
    nums.sort()
    
    n=len(nums)
    
    if n%2==1:
        medv=nums[n//2]
    else:
        medv=(nums[n//2-1]+nums[n//2])/2-1
        
    return medv

data=list(map(int,input().split()))

print(find_median(data))