a=int(input("Enter a range for prime no. :"))
p=[]
for i in range(2,a+1):
    for j in range(2,int(i**(0.5))+1):
        if (i % j) == 0:
            break
    else:
        p.append(str(i))

print(f"prime no. in between 2 and {a} are:"," ".join(p))


print(" ")


num = [int(i) for i in input().split()]
max=0
for i in num:
    if max<=i:
        max=i
print("Largest element is:", max)
