"""
def squareRoot(n, l):
    x = n
    count = 0
    while (1):
        count += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l):
            break
        x = root
    return root
"""


def nm(n, nt = 100):
    a = float(n)
    for i in range(nt):
        n = 0.5 * (n + a / n)
    return n
print("Ritika       2100320130140")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Square root of first number:{0:.3f}".format(nm(a)))
print("Square root of second number:{0:.3f}".format(nm(b)))