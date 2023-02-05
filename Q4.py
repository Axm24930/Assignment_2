lst1=[]
lst2=[]
def unique_lst(x):
    for i in range(n):
        if(int(x[i])>0):
            lst2.append(int(x[i]))

        for j in range(i+1,n):
          if((int(x[i])==int(x[j])) and (int(x[i])>0)):

            x[j]=-(int(x[j]))



n=int(input("Enter the number of elements:"))
for i in range(n):
    print("Enter the element at",i,"index:")
    x=input()
    lst1.append(x)
unique_lst(lst1)
print(lst2)



