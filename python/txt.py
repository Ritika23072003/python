f = open("C:\\Users\\ritik\\OneDrive\\Desktop\\Django.txt","r")
l = f.readline()
count = 0
maxcount =0
l=[]
content = f.read()
wo = content.split()
for i in range(0,len(wo)):
    count = 1
    for j in range(i+1,len(wo)):
        if(wo[i]==wo[j]):
            count = count +1
    if(count > maxcount):
        maxcount = count
        w = wo[i]
print("frequent is : {} word is :{}".format(maxcount,w))
