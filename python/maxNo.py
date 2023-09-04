print("Ritika      2100320130140")
num = [int(i) for i in input().split()]
max=0
for i in num:
    if max<=i:
        max=i
print("Largest element is:", max)
