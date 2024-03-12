#program generates 1 to n where is n is +ve
n=int(input("Enter a number:")) # n=10
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    #logic for generating 1 to n
    print("="*40)
    print("Numbers within:{}".format(n))
    print("=" * 40)
    i=1 # Initlization part
    while(i<=n):   # Cond Part
        print("\t{}".format(i),end="")
        i=i+1 # Updation part
    else:
        print("-" * 40)
