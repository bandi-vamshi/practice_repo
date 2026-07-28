# this is another python file to work with feature branch and merging
# python program to check prime number or not
def even(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
            
    if c>2:
        return f'{n} is not a prime number'
    else:
        return f'{n} is a prime number'
    
print(even(9))


#Python program for two sum

def finding(nums,target):
    
    l=0
    diff=0
    seen={}
    for i,value in enumerate(nums):
        diff=target-value
        if diff in seen:
            return [seen[diff],i]
        
        seen[value]=i
    return []
        
target=10
nums=[2,4,6,8,12,25]
print(finding(nums,target))
            