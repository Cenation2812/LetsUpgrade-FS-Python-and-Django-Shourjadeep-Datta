a=('aaakkk','zzzkkk','iiikkkk','yyyykkkkk','zzkkkk','wwwkkkk')

def func(a): 
    c=0
    for i in range (len(a)):
        b=a[i].count("k")
        print(b)
        if b==1:
            c=c+1
    return c
print(max(a,key= func))
