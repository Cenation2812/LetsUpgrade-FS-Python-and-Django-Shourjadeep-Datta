a=[1,2,3,4,5]
b=["a","b","c","d","e"]
c=[]

for i in range(len(a)) :
    c.append(list((a[i],b[i])))
print(dict(c))
