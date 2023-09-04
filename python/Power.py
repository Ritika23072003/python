print("Ritika       2100320130140")
base = int(input("enter base :"))
exponent = int(input("enter power :"))
result = 1
while exponent != 0:
    result *= base
    exponent-=1
print("Answer = " + str(result))