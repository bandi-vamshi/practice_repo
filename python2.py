# this is another python file to work with feature branch and merging

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
            