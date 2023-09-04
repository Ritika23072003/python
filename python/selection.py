def SS(arr , s):
    for i in range(s):
        m = i
        for j in range(i+1 ,s):
            if arr[j]<arr[m]:
                m = j
        (arr[i], arr[m]) = (arr[m],arr[i])
array = [-34,98,36,2,0,-24,-243]
s = len(array)
SS(array , s)
print("Sorted Array:")
print(array)
print("Ritika         2100320130140")