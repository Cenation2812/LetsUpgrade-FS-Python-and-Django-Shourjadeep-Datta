n=int(input("Enter the number"))
flag=0
if n==1:
      flag=1
else:
      for i in range(2,int((n**.5)+1)):
             if (n%i)==0:
                  print("Not Prime")
                  break
             flag=1
if flag==1:
     print("Prime")

