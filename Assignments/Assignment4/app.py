=[10,20,30,40,10,50,60,10,70,80,10,90,10]
c=0
for i in range(len(l)):
    if  l[i]==10:   
        b=l.index(10,i)
        print(b)
        c=c+1
print("Total occurences of 10 is:",c)
