s="what we think we become we b we was we "
c=0

for i in range(len(s)):
    a=s.find("we")
    if(a>0):
        c+=1
        b=s[a+1:]
        s=b
print(c)
