n=int(input("Enter the Limit "))
s=0
for i in range(1,n+1):
    print("Enter ",i,end='')
    a=int(input("th number : "))
    s=s+a
avg=s/n
print("The sum of entered numbers : ",s)
print("The Average of entered numbers : ",avg)