n=int(input("Enter the Limit : "))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print("*",end='')
    print("")    
