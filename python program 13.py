n=int(input("Enter the Limit less than 99999999999 "))
small=99999999999
for i in range(1,n+1):
    print("Enter ",i,end='')
    a=int(input("th number : "))
    if a<small:
        small=a
print("Second largest element is:",a[n-2])        
        
    
    
