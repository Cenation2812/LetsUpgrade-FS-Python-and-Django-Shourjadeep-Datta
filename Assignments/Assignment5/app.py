l2=[10,20,30,40,50,60,70,80,90]
l1=[5,15,25,35,45,55,65,75,85,95,96,97]
l=[]

if len(l1)>len(l2):
        l1.extend(l2[:])
        a=len(l1)

else:
        l2.extend(l1[:])
        a=len(l2)
  
b=len(l1)
for i in range(a):
        if a==b:
            s=min(l1)
            l.append(s)
            l1.remove(s)
        else:
            s=min(l2)
            l.append(s)
            l2.remove(s)
print(l)

