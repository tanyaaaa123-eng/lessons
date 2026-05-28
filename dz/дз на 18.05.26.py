nums = [1,3,4,5,3]
target=7
def f(nums,target):
    l=0
    summ=0
    min_l = float("inf")#огромное число просто
    for right in range(len(nums)):
        summ+=nums[right]
        l = right-l+1
        while summ >=target:
            summ -=nums[l]
            l+=1
            min_l=min(min_l,l)
    return min_l if min_l!=float("inf")else 0
#
def f1(height):
    left=0
    right = len(height)-1

nums = [-4,-1,0,3,10]

def f3(nums):
    l =0
    c=[]
    maxx=-1
    r=len(nums)-1
    while l<=r:
        c.append(nums[l]**2)
        l+=1
       if maxx=max(maxx,nums[l]**2):
            c[0]=c[]


    return c
print(f3([-4,-1,0,3,10]))





