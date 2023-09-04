
a=int(input("Enter a range for prime no. :"))
p=[]
for i in range(2,a+1):
    for j in range(2,int(i**(0.5))+1):
        if (i % j) == 0:
            break
    else:
        p.append(str(i))

print(f"prime no. in between 2 and {a} are:"," ".join(p))
print("Ritika    2100320130140")













# print(" ")
# numr=int(input("Enter range:"))
#
# print("Prime numbers:",end=' ')
#
# for n in range(1,numr):
#
#     for i in range(2,n):
#
#         if(n%i==0):
#
#             break
#     else:
#         print(n,end=' ')
#

