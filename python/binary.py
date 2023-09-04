def bs(arr, low, high, x):
    if high>=low:
        mid =(high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x :
            return bs(arr,low,mid-1,x)
        else:
            return bs(arr,mid+1,high,x)
    else:
        return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x= 100
r = bs(arr, 0,len(arr)-1,x)
if r!=-1:
    print("element is found at index",str(r))
else:
    print("element is not present")
print("Ritika       2100320130140")
