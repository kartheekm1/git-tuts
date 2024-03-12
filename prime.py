n=int(input("Enter the n value"))
n1=2
count=1
while(count<=n):
    is_prime=True
    for i in range(2,n1):
        if n1%i==0:
            is_prime=False
            break
    if(is_prime==True):
        print(n1)
        count=count+1
    n1=n1+1
