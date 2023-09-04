"""
def IS(arr):
    if(n:= len(arr)) <= 1:
        return
    for i in range(1, n):
        k = arr[i]
        j = i-1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
arr= [12,3,6,13,56,890,5,67]
IS(arr)
print("Sorted Array:")
print(arr)
"""


def insertion(arr):
    for step in range(1,len(arr)):
        key = arr[step]
        j = step-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1]=key
a= [-1,-34,12,3,6,13,56,890,5,67]
insertion(a)
print("Sorted Array:")
print(a)
print("Ritika       2100320130140")







