def linear(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 30
r = linear(arr, x)
if(r == -1):
    print("Element not found")
else:
    print("Element is found at index",r)

print("RITIKA         210032010140")
